import os
import random
import re
from typing import Dict, Any, List, Optional

from flask import (
    Flask,
    jsonify,
    render_template,
    request,
    abort,
    redirect,
    url_for,
    flash,
)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, inspect

# -----------------------------------------------------------------------------
# Config (DB path resolved relative to this file, with override via env var)
# -----------------------------------------------------------------------------

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DEFAULT_DB = os.path.join(BASE_DIR, "cafes.db")
DB_FILE = os.environ.get("CAFES_DB_PATH", DEFAULT_DB)

ADMIN_API_KEY = os.environ.get("ADMIN_API_KEY", "TopSecretAPIKey")  # for DELETE (API & UI)
SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret")             # for flash messages

# -----------------------------------------------------------------------------
# App + DB setup (SQLAlchemy 2.0 style)
# -----------------------------------------------------------------------------

class Base(DeclarativeBase):
    pass

app = Flask(__name__)
app.config["SECRET_KEY"] = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_FILE}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(model_class=Base)
db.init_app(app)

# -----------------------------------------------------------------------------
# Model
# -----------------------------------------------------------------------------

class Cafe(db.Model):
    __tablename__ = "cafes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[Optional[str]] = mapped_column(String(50))
    has_toilet: Mapped[bool] = mapped_column(Boolean, default=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, default=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, default=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, default=False)
    coffee_price: Mapped[Optional[str]] = mapped_column(String(50))

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "name": self.name,
            "map_url": self.map_url,
            "img_url": self.img_url,
            "location": self.location,
            "seats": self.seats,
            "has_toilet": self.has_toilet,
            "has_wifi": self.has_wifi,
            "has_sockets": self.has_sockets,
            "can_take_calls": self.can_take_calls,
            "coffee_price": self.coffee_price,
        }

# -----------------------------------------------------------------------------
# Ensure the 'cafes' table exists (helpful if you accidentally pointed to a fresh DB)
# -----------------------------------------------------------------------------

with app.app_context():
    insp = inspect(db.engine)
    if not insp.has_table("cafes"):
        # If you're using the provided populated cafes.db, this will be a no-op.
        # If you pointed at a new/empty file, this will create the schema so the app runs.
        db.create_all()

# -----------------------------------------------------------------------------
# HTML PAGES (UI)
# -----------------------------------------------------------------------------

@app.route("/")
def home():
    # Simple landing page with CTA button → /cafes
    return render_template("index.html")

@app.route("/cafes")
def cafes_ui():
    """
    Render a list of cafes with optional filters via querystring:
    ?loc=&wifi=on&sockets=on&toilet=on&calls=on&min_seats=10
    """
    q = db.session.query(Cafe)

    loc = request.args.get("loc")
    if loc:
        q = q.filter(Cafe.location.ilike(f"%{loc}%"))

    if request.args.get("wifi"):
        q = q.filter(Cafe.has_wifi.is_(True))
    if request.args.get("sockets"):
        q = q.filter(Cafe.has_sockets.is_(True))
    if request.args.get("toilet"):
        q = q.filter(Cafe.has_toilet.is_(True))
    if request.args.get("calls"):
        q = q.filter(Cafe.can_take_calls.is_(True))

    cafes: List[Cafe] = q.all()

    # seats stored as a string (e.g., "10+", "20"), approximate numeric filtering
    min_seats = request.args.get("min_seats")
    if min_seats:
        try:
            min_val = int(min_seats)

            def seats_num(s: Optional[str]) -> int:
                if not s:
                    return 0
                m = re.search(r"\d+", s)
                return int(m.group()) if m else 0

            cafes = [c for c in cafes if seats_num(c.seats) >= min_val]
        except ValueError:
            pass

    return render_template("cafes.html", cafes=cafes, filters=request.args)

@app.route("/cafes/<int:id>")
def cafe_detail_ui(id: int):
    cafe = db.session.get(Cafe, id)
    if not cafe:
        abort(404)
    return render_template("cafe_detail.html", cafe=cafe)

@app.route("/ui/add", methods=["GET", "POST"])
def add_cafe_ui():
    if request.method == "POST":
        # Accept data from form
        cafe = Cafe(
            name=request.form["name"],
            map_url=request.form["map_url"],
            img_url=request.form["img_url"],
            location=request.form["location"],
            seats=request.form["seats"],
            has_toilet=("has_toilet" in request.form),
            has_wifi=("has_wifi" in request.form),
            has_sockets=("has_sockets" in request.form),
            can_take_calls=("can_take_calls" in request.form),
            coffee_price=request.form.get("coffee_price") or None,
        )
        try:
            db.session.add(cafe)
            db.session.commit()
            flash("Cafe added successfully.", "success")
            return redirect(url_for("cafes_ui"))
        except Exception as e:
            db.session.rollback()
            flash(f"Database error: {e}", "danger")

    return render_template("add_cafe.html")

@app.route("/ui/update-price/<int:id>", methods=["POST"])
def update_price_ui(id: int):
    cafe = db.session.get(Cafe, id)
    if not cafe:
        abort(404)

    new_price = request.form.get("new_price")
    if not new_price:
        flash("Missing new price.", "warning")
        return redirect(url_for("cafe_detail_ui", id=id))

    cafe.coffee_price = new_price
    db.session.commit()
    flash("Coffee price updated.", "success")
    return redirect(url_for("cafe_detail_ui", id=id))

@app.route("/ui/delete/<int:id>", methods=["GET", "POST"])
def delete_cafe_ui(id: int):
    cafe = db.session.get(Cafe, id)
    if not cafe:
        abort(404)

    if request.method == "POST":
        admin_key = request.form.get("admin_key")
        if admin_key != ADMIN_API_KEY:
            flash("Invalid admin key.", "danger")
            return redirect(url_for("delete_cafe_ui", id=id))

        db.session.delete(cafe)
        db.session.commit()
        flash("Cafe deleted.", "success")
        return redirect(url_for("cafes_ui"))

    return render_template("delete_cafe.html", cafe=cafe)

# -----------------------------------------------------------------------------
# JSON API
# -----------------------------------------------------------------------------

@app.route("/random")
def random_cafe():
    cafes = db.session.query(Cafe).all()
    if not cafes:
        return jsonify(error={"Not Found": "No cafes available."}), 404
    cafe = random.choice(cafes)
    return jsonify(cafe=cafe.to_dict())

@app.route("/all")
def all_cafes():
    cafes = db.session.query(Cafe).all()
    return jsonify(cafes=[c.to_dict() for c in cafes])

@app.route("/search")
def search():
    """Example: /search?loc=London"""
    query_location = request.args.get("loc")
    if not query_location:
        return jsonify(error={"Bad Request": "Missing 'loc' parameter."}), 400

    cafes = (
        db.session.query(Cafe)
        .filter(Cafe.location.ilike(f"%{query_location}%"))
        .all()
    )
    if cafes:
        return jsonify(cafes=[c.to_dict() for c in cafes])
    return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404

@app.route("/add", methods=["POST"])
def add():
    """
    Accepts form-encoded or JSON payloads.
    Required: name, map_url, img_url, location
    Optional: seats, has_toilet, has_wifi, has_sockets, can_take_calls, coffee_price
    """
    data = request.form if request.form else request.json or {}

    required = ["name", "map_url", "img_url", "location"]
    missing = [k for k in required if not data.get(k)]
    if missing:
        return jsonify(error={"Bad Request": f"Missing fields: {', '.join(missing)}"}), 400

    def to_bool(val: Any) -> bool:
        if isinstance(val, bool):
            return val
        if isinstance(val, str):
            return val.lower() in {"1", "true", "yes", "on"}
        return False

    new_cafe = Cafe(
        name=data["name"],
        map_url=data["map_url"],
        img_url=data["img_url"],
        location=data["location"],
        seats=data.get("seats"),
        has_toilet=to_bool(data.get("has_toilet")),
        has_wifi=to_bool(data.get("has_wifi")),
        has_sockets=to_bool(data.get("has_sockets")),
        can_take_calls=to_bool(data.get("can_take_calls")),
        coffee_price=data.get("coffee_price"),
    )

    try:
        db.session.add(new_cafe)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return jsonify(error={"Database Error": str(e)}), 500

    return jsonify(response={"success": "Successfully added the new cafe."}), 201

@app.route("/update/<int:id>", methods=["PATCH"])
def update_price(id: int):
    """
    Update coffee price.
    Accepts ?new_price=... OR JSON {"new_price": "..."}
    """
    new_price = request.args.get("new_price")
    if not new_price and request.is_json:
        new_price = (request.json or {}).get("new_price")

    cafe = db.session.get(Cafe, id)
    if not cafe:
        return jsonify(error={"Not Found": "Sorry, no cafe with that ID was found."}), 404

    if not new_price:
        return jsonify(error={"Bad Request": "Missing new_price parameter."}), 400

    cafe.coffee_price = new_price
    db.session.commit()
    return jsonify(response={"success": "Successfully updated the price."}), 200

@app.route("/report-closed/<int:id>", methods=["DELETE"])
def delete(id: int):
    """
    Delete a cafe (requires api-key in querystring or JSON body).
    Example: /report-closed/3?api-key=TopSecretAPIKey
    """
    api_key = request.args.get("api-key")
    if not api_key and request.is_json:
        api_key = (request.json or {}).get("api-key")

    if api_key != ADMIN_API_KEY:
        return jsonify(error={"Unauthorized": "Invalid API Key."}), 403

    cafe = db.session.get(Cafe, id)
    if not cafe:
        return jsonify(error={"Not Found": "No cafe with that ID was found."}), 404

    db.session.delete(cafe)
    db.session.commit()
    return jsonify(response={"success": "Cafe deleted successfully."}), 200

# -----------------------------------------------------------------------------
# Debug helper (optional): see which DB and tables you're hitting
# -----------------------------------------------------------------------------

@app.route("/__dbinfo")
def __dbinfo():
    with app.app_context():
        insp = inspect(db.engine)
        return {
            "db_uri": app.config["SQLALCHEMY_DATABASE_URI"],
            "tables": insp.get_table_names(),
            "db_exists": os.path.exists(DB_FILE),
        }

# -----------------------------------------------------------------------------
# Entrypoint
# -----------------------------------------------------------------------------

if __name__ == "__main__":
    # If you're deliberately starting with an empty DB, the create_all() above has already run.
    app.run(debug=True)
