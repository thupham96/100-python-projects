from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = '<your_secret_key>'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///favorite-movies.db"

Bootstrap5(app)

MOVIE_DATABASE_KEY = '<your_movie_database_key>'
MOVIE_SEARCH_URL = 'https://api.themoviedb.org/3/search/movie'

headers = {
    "accept": "application/json",
    "Authorization": "<your_authentication>"
}

# Database setup
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)
db.init_app(app)

class Movie(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    description: Mapped[str] = mapped_column(String(2000), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)
    ranking: Mapped[int] = mapped_column(Integer, nullable=False)
    review: Mapped[str] = mapped_column(String(2000), nullable=False)
    img_url: Mapped[str] = mapped_column(String(1000), nullable=False)

    def __repr__(self):
        return f'<Movie {self.title}>'

# Forms
class EditForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5", validators=[DataRequired()])
    review = StringField("Your Review", validators=[DataRequired()])
    submit = SubmitField("Done")

class AddForm(FlaskForm):
    movie_title = StringField("Movie Title", validators=[DataRequired()])
    add = SubmitField("Add Movie")

# Routes
@app.route("/")
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    all_movies = list(result.scalars())
    for i in range(len(all_movies)):
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)

@app.route("/update/<int:movie_id>", methods=["GET", "POST"])
def update(movie_id):
    form = EditForm()
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    form.rating.data = str(movie.rating)
    form.review.data = movie.review
    return render_template("edit.html", form=form, movie=movie)

@app.route("/delete/<int:movie_id>", methods=["POST"])
def delete(movie_id):
    movie = db.get_or_404(Movie, movie_id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddForm()
    if form.validate_on_submit():
        params = {"query": form.movie_title.data}
        response = requests.get(MOVIE_SEARCH_URL, headers=headers, params=params)
        data = response.json()
        movies = data["results"]
        return render_template("select.html", movies=movies)
    return render_template("add.html", form=form)

@app.route("/select/<int:movie_id>")
def select(movie_id):
    MOVIE_DETAILS_URL = f'https://api.themoviedb.org/3/movie/{movie_id}'
    response = requests.get(MOVIE_DETAILS_URL, headers=headers)
    data = response.json()
    new_movie = Movie(
        title=data["title"],
        year=int(data["release_date"][:4]),
        description=data["overview"],
        rating=0,
        ranking=0,
        review="",
        img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}"
    )
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for("update", movie_id=new_movie.id))

if __name__ == '__main__':
    app.run(debug=True)
