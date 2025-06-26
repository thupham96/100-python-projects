# Day 69: Flask Blog CMS – Admin-Only Editor with Comments

A Flask-based blog platform with full CRUD functionality, rich-text editing, user authentication, admin-only post management, and a comment system. Built using **Flask**, **Flask-Login**, **SQLAlchemy**, **CKEditor**, and **Gravatar** integration.

---

## Overview

**Flask Blog CMS** enables users to:

* Register and log in securely
* Create, edit, and delete posts (admin-only)
* Write rich-text blog posts with images
* Comment on posts after logging in
* View Gravatar profile images beside comments
* Manage user sessions and protect admin routes

---

## Run the App

```bash
python main.py
```

Then go to:

```
http://127.0.0.1:5002/
```

---

## Setup Instructions

1. **Clone the repository and navigate:**

   ```bash
   git clone https://github.com/yourusername/100-python-projects.git
   cd Day69_FlaskBlogCMS
   ```

2. **Install dependencies:**

   ```bash
   pip install flask flask_sqlalchemy flask_login flask_bootstrap flask_wtf flask_ckeditor flask_gravatar
   ```

3. **Ensure the following folders exist:**

   ```
   /static/assets/img/
   ```

4. **Run the application:**

   ```bash
   python main.py
   ```

---

## Key Routes

| Route                | Methods  | Description                                |
| -------------------- | -------- | ------------------------------------------ |
| `/`                  | GET      | View all blog posts                        |
| `/register`          | GET/POST | Register new users                         |
| `/login`             | GET/POST | Log in users                               |
| `/logout`            | GET      | Log out users                              |
| `/post/<post_id>`    | GET/POST | View post + leave a comment (if logged in) |
| `/new-post`          | GET/POST | Admin-only: create a new post              |
| `/edit-post/<id>`    | GET/POST | Admin-only: edit an existing post          |
| `/delete/<id>`       | GET      | Admin-only: delete a post                  |
| `/about`, `/contact` | GET      | Static info pages                          |

---

## User Model

```python
id: int
email: str (unique)
password: str (hashed)
name: str
```

---

## Features

* Secure user auth with `Flask-Login` and `werkzeug.security`
* CKEditor for blog and comment input
* Admin-only control over post creation and editing
* Commenting system with email-based Gravatars
* Flash messaging for login and registration feedback
* Post metadata like title, subtitle, image, author, and date

---

## What I Learned

* Implementing user and session management with Flask-Login
* Using decorators to restrict admin-only routes
* Creating relational models with SQLAlchemy ORM
* Integrating CKEditor and Gravatar in a Flask app
* Handling form validation and flash messages

---

📚 Build your own fully-functional blog with admin access and rich user interaction using Flask!
