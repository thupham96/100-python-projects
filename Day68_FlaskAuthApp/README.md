# Day 68: 🔐 Flask Auth App – User Registration & Login System 👤🔑

A secure and beginner-friendly Flask application that implements user registration, login, session management, and protected file download. It uses **Flask-Login**, **SQLAlchemy**, and **Werkzeug security** for password hashing.

---

## 📖 Overview

**Flask Auth App** allows users to:

* 📝 Register with name, email, and password
* 🔐 Log in with authentication checks
* 🔓 Access a protected page after login
* 📄 Download a file only after logging in
* 🚪 Log out securely

---

## 🚀 Run the App

```bash
python main.py
```

Then visit:

```
http://127.0.0.1:5000/
```

---

## 📁 Setup Instructions

1. **Clone the repository and navigate to the folder:**

   ```bash
   git clone https://github.com/yourusername/100-python-projects.git
   cd Day68_FlaskAuthApp
   ```

2. **Install dependencies:**

   ```bash
   pip install flask flask_sqlalchemy flask_login
   ```

3. **Ensure a folder `static/files/` exists and contains `cheat_sheet.pdf`.**

4. **Run the app:**

   ```bash
   python main.py
   ```

---

## 🔐 Key Routes

| Route       | Methods  | Description                             |
| ----------- | -------- | --------------------------------------- |
| `/`         | GET      | Homepage                                |
| `/register` | GET/POST | User registration with password hashing |
| `/login`    | GET/POST | User login with session authentication  |
| `/secrets`  | GET      | Protected welcome page                  |
| `/download` | GET      | Authenticated file download             |
| `/logout`   | GET      | Logs the user out                       |

---

## 👥 User Model

```python
id: int
name: str
email: str (unique)
password: str (hashed)
```

---

## 🔧 Features

* 🔐 Secure password storage using `werkzeug.security`
* ✅ Authentication via `Flask-Login`
* 📂 Protected downloads and session checks
* 🧱 SQLite + SQLAlchemy for persistent storage
* 💬 Flash messages for login/registration errors

---

## 🧠 What I Learned

* How to manage user sessions with Flask-Login
* Storing passwords securely with hashing
* Creating protected routes requiring login
* Handling flash messaging for UX feedback
* Using SQLAlchemy ORM for user models

---

🔒 Build your own secure user login system with Flask and give users access to exclusive content!
