# Day 67: 📝 Blog Post CMS – Flask + SQLAlchemy + CKEditor 💡🖋️

A lightweight content management system (CMS) for blogging, built using **Flask**, **SQLAlchemy**, **Flask-WTF**, and **CKEditor**. This project enables users to create, read, update, and delete blog posts through a clean Bootstrap-themed web interface.

---

## 📖 Overview

**Blog Post CMS** is a personal blogging platform where users can:

* 🆕 Create rich-text blog posts with images
* ✏️ Edit or update existing posts
* ❌ Delete posts when needed
* 📄 View posts in a styled template
* 📬 Access About and Contact pages

---

## 🚀 Run the App

```bash
python main.py
```

Then open your browser at:

```
http://127.0.0.1:5003/
```

---

## 📁 Setup Instructions

1. **Clone the repository and navigate to the folder:**

   ```bash
   git clone https://github.com/yourusername/100-python-projects.git
   cd Day67_BlogPostCMS
   ```

2. **Install required dependencies:**

   ```bash
   pip install flask flask_sqlalchemy flask_bootstrap flask_wtf flask_ckeditor
   ```

3. **Run the application:**

   ```bash
   python main.py
   ```

---

## 🗺️ Routes & Features

| Route                  | Method     | Description                            |
| ---------------------- | ---------- | -------------------------------------- |
| `/`                    | GET        | Homepage showing all blog posts        |
| `/new-post`            | GET/POST   | Add a new blog post with CKEditor form |
| `/<int:post_id>`       | GET        | View a specific post                   |
| `/edit-post/<post_id>` | GET/POST   | Edit a post using pre-filled form      |
| `/delete/<post_id>`    | GET/DELETE | Delete a blog post                     |
| `/about`               | GET        | About page                             |
| `/contact`             | GET        | Contact form (not used in Day 67)      |

---

## 🧾 BlogPost Model

```python
id: int
title: str
subtitle: str
author: str
img_url: str
body: str
date: str
```

---

## 💡 Features

* ✅ Fully functional CRUD operations
* 🖋️ Rich text editing with Flask-CKEditor
* 🎨 Responsive Bootstrap styling
* 🧩 Modular HTML templates (`header`, `footer`, etc.)
* 📆 Automatic post dating with `datetime.date`

---

## 🧠 What I Learned

* Building a Flask CMS with SQLAlchemy ORM
* Using WTForms for form handling and validation
* Integrating CKEditor into Flask forms
* Template inheritance and modular HTML components
* Implementing safe deletion and URL routing

---

📰 Turn your thoughts into posts and manage your blog with this simple yet powerful Flask CMS!
