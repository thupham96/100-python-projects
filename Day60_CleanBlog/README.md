# Day 60: ✨ Clean Blog – Flask Blogging Platform 📝🌐

A sleek and responsive blog application built with **Flask**, **HTML**, **CSS**, and **Bootstrap**, integrating dynamic blog post content via a JSON API and featuring a fully functional contact form with email integration.

---

## 📖 Overview

**Clean Blog** is a minimalist, elegant blogging platform powered by Python and Flask. It fetches posts from an external JSON source and dynamically renders them across multiple routes. The application includes dedicated pages for About and Contact, using modular templates for clean code reuse.

---

## 🚀 Live Preview

```bash
python main.py
```

Then navigate to:
`http://localhost:5001/`

---

## 🗺️ Routes & Features

| Route        | Description                                 |
| ------------ | ------------------------------------------- |
| `/`          | Homepage listing all blog posts             |
| `/post/<id>` | Individual blog post view with full content |
| `/about`     | Static About Me page                        |
| `/contact`   | Contact form with email functionality       |

---

## 💡 Key Features

* 📃 Dynamic blog rendering using Flask + Jinja2 templating
* 🌐 External JSON API integration (via [npoint.io](https://api.npoint.io/c790b4d5cab58020d391))
* ✉️ Contact form sending messages via SMTP (Gmail)
* 🧩 Modular HTML templates with `header.html` and `footer.html`
* 📱 Responsive Bootstrap 5 layout
* 🖼️ Background images for each page
* 📩 Confirmation message after successful form submission

---

## 📁 Project Structure

```
Day60_CleanBlog/
├── main.py
├── templates/
│   ├── index.html
│   ├── post.html
│   ├── about.html
│   ├── contact.html
│   ├── form-entry.html
│   ├── header.html
│   └── footer.html
├── static/
│   ├── assets/
│   │   └── img/
│   │       ├── home-bg.jpg
│   │       ├── about-bg.jpg
│   │       ├── contact-bg.jpg
│   └── css/
│       └── styles.css
```

---

## ⚙️ How to Use

1. **Clone the repository:**

   ```bash
   git clone https://github.com/thupham96/100-python-projects.git
   cd Day60_CleanBlog
   ```

2. **Install dependencies:**

   ```bash
   pip install flask
   ```

3. **Run the Flask app:**

   ```bash
   python main.py
   ```

4. **Open your browser at:**

   ```
   http://127.0.0.1:5001/
   ```

---

## 🔐 Note on Email Credentials

This app uses SMTP with Gmail to send form entries. For production use:

* Replace `my_email` and `my_password` with environment variables.
* Use a secure app password.
* Avoid committing credentials to version control.

---

## 🧰 Technologies Used

* Python (Flask)
* HTML5 + Jinja2
* CSS3
* Bootstrap 5
* Font Awesome Icons
* Google Fonts

---

## 🧠 What I Learned

* Creating a Flask app with multiple routes and templates
* Rendering JSON API data dynamically
* Sending emails with Python’s `smtplib`
* Using Jinja2 includes for reusable HTML components
* Styling and responsiveness with Bootstrap

---

✨ Share your voice with the world — one clean blog post at a time.
