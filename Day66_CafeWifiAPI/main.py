import random

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean

'''
Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''

app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


# HTTP GET - Read Record
@app.route("/random")
def get_random_cafe():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    random_cafe = random.choice(all_cafes)
    return jsonify(cafe=random_cafe.to_dict())

@app.route("/all")
def get_all_cafes():
    result = db.session.execute(db.select(Cafe))
    all_cafes = result.scalars().all()
    return jsonify(cafes=[cafe.to_dict() for cafe in all_cafes])

@app.route("/search")
def search():
    location = request.args.get("loc")
    result = db.session.execute(db.select(Cafe).where(Cafe.location.like(f"%{location}%")))
    filtered_cafes = result.scalars().all()
    if not filtered_cafes:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404
    return jsonify(cafes=[cafe.to_dict() for cafe in filtered_cafes])

# HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("location"),
        seats=request.form.get("seats"),
        has_toilet=bool(int(request.form.get("has_toilet"))),
        has_wifi=bool(int(request.form.get("has_wifi"))),
        has_sockets=bool(int(request.form.get("has_sockets"))),
        can_take_calls=bool(int(request.form.get("can_take_calls"))),
        coffee_price=request.form.get("coffee_price")
    )

    try:
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify(response={"success": "Successfully added the new cafe."}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify(error={"Database error": str(e)}), 500

# HTTP PUT/PATCH - Update Record
@app.route("/update/<int:id>", methods=["PATCH"])
def update_price(id):
    new_price = request.args.get("new_price")
    cafe = db.session.get(Cafe, id)

    if not cafe:
        return jsonify(error={"Not Found": "Sorry, no cafe with that ID was found."}), 404

    if not new_price:
        return jsonify(error={"Bad Request": "Missing new_price parameter."}), 400

    cafe.coffee_price = new_price
    db.session.commit()

    return jsonify(response={"success": "Coffee price updated successfully."}), 200

# HTTP DELETE - Delete Record
@app.route("/report-closed/<int:id>", methods=["DELETE"])
def delete(id):
    api_key = request.args.get("api-key")
    if api_key!="TopSecretAPIKey":
        return jsonify(error={"Unauthorized": "Invalid API Key."}), 403

    cafe = db.session.get(Cafe, id)
    if not cafe:
        return jsonify(error={"Not Found": "No cafe with that ID was found."}), 404
    db.session.delete(cafe)
    db.session.commit()
    return jsonify(response={"success": "Cafe deleted successfully."}), 200

if __name__ == '__main__':
    app.run(debug=True)
