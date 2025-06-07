# Day 63: 📚 Book Library – Flask App with SQLite & WTForms

A lightweight Flask web application for managing a personal book collection. Users can add new books with a title, author, and rating, view them in a sortable list, and edit their ratings directly.

---

## 📖 Overview

**Book Library** is a basic full-stack Flask app that allows users to:

* Submit new books using a Bootstrap-enhanced form
* Store book data persistently in a SQLite database via SQLAlchemy
* Edit the rating of any book via a dedicated update page

---

## 🚀 Quick Start

```bash
python main.py
```

Then open:

```
http://127.0.0.1:5000/
```

---

## 🗺️ Routes & Features

| Route             | Description                       |
| ----------------- | --------------------------------- |
| `/`               | Home page – displays all books    |
| `/add`            | Form to add a new book            |
| `/edit/<book_id>` | Update rating for a specific book |

---

## 💡 Key Features

* 📝 WTForms-powered form with input validation
* 📊 Ratings stored as floats in a SQLite database
* ⚡ SQLAlchemy ORM with auto-generated schema
* 🎨 Clean and responsive UI via Flask-Bootstrap 5
* 🔄 Update book ratings with a simple POST form

---

## 📁 Project Structure

```
Day63_BookLibrary/
├── main.py
├── templates/
│   ├── index.html
│   ├── add.html
│   └── edit.html
├── static/
│   └── (optional for CSS/images)
├── new-books-c.db
```

---

## ⚙️ Setup & Installation

1. **Clone or download the project:**

   ```bash
   git clone https://github.com/yourusername/100-python-projects.git
   cd Day63_BookLibrary
   ```

2. **Install required libraries:**

   ```bash
   pip install flask flask-wtf flask-bootstrap flask-sqlalchemy
   ```

3. **Run the app:**

   ```bash
   python main.py
   ```

---

## 🧠 What I Learned

* Setting up a Flask app with SQLAlchemy and declarative base
* Creating WTForms with Flask-WTF and validators
* Connecting routes to forms for both creation and update
* Managing basic GET and POST logic in Flask views
* Rendering templates with Jinja2 and pre-filled form data

---

📚 Build and maintain your personal library — one book at a time!
