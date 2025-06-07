# Day 64: 🎬 Favorite Movies Catalog – Flask + TMDB API 🎥🍿

A Flask-based web application that allows users to build and manage a list of favorite movies. It integrates with the TMDB API to search movie details and uses a SQLAlchemy-powered SQLite database to store ratings, reviews, and metadata.

---

## 📖 Overview

**Favorite Movies Catalog** is a dynamic web app where users can:

* Search movies via the TMDB API
* Add selected movies to their personal list
* Rate, review, and rank their favorites
* View a styled table of all movies with posters

---

## 🚀 Run the App

```bash
python main.py
```

Visit:

```
http://127.0.0.1:5000/
```

---

## 🗺️ Routes & Features

| Route                | Description                                 |
| -------------------- | ------------------------------------------- |
| `/`                  | Homepage displaying all favorite movies     |
| `/add`               | Search for a new movie by title             |
| `/select/<movie_id>` | Add a selected movie with details from TMDB |
| `/update/<movie_id>` | Edit rating and review for a specific movie |
| `/delete/<movie_id>` | Delete a movie from the catalog (POST only) |

---

## 💡 Key Features

* 🔍 Movie search powered by **TMDB API**
* 🎯 Add movie by selecting from search results
* ⭐ Custom rating and review per movie
* 🏆 Dynamic ranking based on rating
* 🖼️ Movie posters from TMDB displayed
* 🧾 SQLite + SQLAlchemy for structured data storage
* 🎨 Responsive Bootstrap 5 UI with Flask-Bootstrap
* ✅ WTForms for form handling and validation

---

## 📁 Project Structure

```
Day64_FavoriteMovies/
├── main.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── add.html
│   ├── edit.html
│   └── select.html
├── static/
│   └── (optional CSS/images)
├── favorite-movies.db
```

---

## ⚙️ Setup Instructions

1. **Clone the repository or copy the files:**

   ```bash
   git clone https://github.com/yourusername/100-python-projects.git
   cd Day64_FavoriteMovies
   ```

2. **Install the required packages:**

   ```bash
   pip install flask flask-bootstrap flask-wtf flask-sqlalchemy requests
   ```

3. **Run the app:**

   ```bash
   python main.py
   ```

---

## 🔐 Environment Notes

* API key and bearer token for TMDB are embedded in the source for educational/demo purposes.
* Replace `Authorization` header with your own secure TMDB access token for production use.

---

## 🧠 What I Learned

* Integrating Flask with external APIs (TMDB)
* Building a full CRUD app with Flask & SQLAlchemy
* Using WTForms with Bootstrap 5 for clean, validated forms
* Designing a dynamic ranking algorithm based on user input
* Structuring RESTful routes in a Flask project

---

🎥 Create your ultimate movie list, share reviews, and rank your favorite flicks — all from your browser!
