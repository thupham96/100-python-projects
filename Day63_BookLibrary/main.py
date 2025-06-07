from flask import Flask, render_template, request, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, SubmitField
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)
app.config['SECRET_KEY'] = '<your_secret_key>'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///new-books-c.db"
Bootstrap5(app)

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    rating: Mapped[float] = mapped_column(Float, unique=True, nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'

class BookForm(FlaskForm):
    book_name = StringField("Book Name", validators=[DataRequired()])
    book_author = StringField("Book Author", validators=[DataRequired()])
    book_rating = StringField("Book Rating", validators=[DataRequired()])
    add_button = SubmitField("Add Book")

@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = list(result.scalars())
    return render_template("index.html", books=all_books)

@app.route("/add", methods=["GET", "POST"])
def add():
    form = BookForm()
    if form.validate_on_submit():
        new_book = Book(
            title=form.book_name.data,
            author=form.book_author.data,
            rating=float(form.book_rating.data)
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html", form=form)

@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit(book_id):
    print(book_id)
    book = db.get_or_404(Book, book_id)
    render_template("edit.html", book=book)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
