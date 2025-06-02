# Day 61: 🔐 Secrets – Flask Login Form App 🕵️‍♀️✨

A beginner-friendly Flask application that demonstrates secure login validation using **WTForms**, **Flask-WTF**, and **Bootstrap 5**. It restricts access to a “secret” page and provides fun visual feedback for both success and denial scenarios.

---

## 📖 Overview

**Secrets App** is a mini Flask web application that showcases how to build and validate a login form using Flask-WTF. Upon entering the correct credentials, users are redirected to a success page with a secret message. Incorrect logins lead to an “Access Denied” page — complete with GIFs!

---

## 🚀 Live Preview

```bash
python main.py
```

Then navigate to:
`http://localhost:5000/`

---

## 🗺️ Routes & Features

| Route     | Description                                     |
| --------- | ----------------------------------------------- |
| `/`       | Home page with a call to action to log in       |
| `/login`  | Form page for email and password authentication |
| `success` | Rendered if login credentials are valid         |
| `denied`  | Rendered if credentials do not match            |

---

## 💡 Key Features

* ✍️ WTForms with built-in validation for:

  * Required fields
  * Valid email format
  * Minimum password length
* 🎨 Styled with Flask-Bootstrap for clean UI
* 🔐 Secret key configuration for CSRF protection
* ✅ Logic to verify hardcoded credentials (`admin@email.com` + `12345678`)
* 📺 Embedded GIFs on success/denied pages for a fun touch

---

## 📁 Project Structure

```
Day61_SecretsApp/
├── main.py
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── login.html
│   ├── success.html
│   └── denied.html
└── static/
    └── (Optional assets)
```

---

## ⚙️ How to Use

1. **Clone or download the project:**

   ```bash
   git clone https://github.com/yourusername/100-python-projects.git
   cd Day61_SecretsApp
   ```

2. **Install the necessary packages:**

   ```bash
   pip install flask flask-wtf flask-bootstrap
   ```

3. **Run the Flask server:**

   ```bash
   python main.py
   ```

4. **Test credentials at:**

   ```
   http://127.0.0.1:5000/login
   ```

   Use:

   * Email: `admin@email.com`
   * Password: `12345678`

---

## 🧰 Technologies Used

* Flask
* Flask-WTF + WTForms
* Flask-Bootstrap
* HTML5 & Jinja2
* GIPHY embeds for page feedback

---

## 🧠 What I Learned

* Setting up and validating secure forms in Flask
* Applying Bootstrap layout with `Flask-Bootstrap`
* Managing conditional logic for login success/failure
* Using Jinja2 to modularize templates
* Serving fun and dynamic content using embedded media

---

💡 Keep your secrets safe — unless you want to rickroll someone 😏
