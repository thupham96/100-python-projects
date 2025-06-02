# Day 62: ☕ Cafe & Wifi – Flask Form + CSV Database 🌐📋

A Flask-based web application that allows users to add and browse cafés with ratings for coffee, wifi strength, and power outlet availability. It features a Bootstrap-powered form, CSV-based storage, and a dynamic data table display.

---

## 📖 Overview

**Cafe & Wifi** is a simple full-stack application for café enthusiasts to share and discover café locations. Users can submit a new café through a form, which gets saved into a CSV file. All submitted cafés are displayed in a styled table format with clickable Google Maps links.

---

## 🚀 Live Preview

```bash
python main.py
```

Then visit:
`http://localhost:5000/`

---

## 🗺️ Routes & Features

| Route    | Description                                    |
| -------- | ---------------------------------------------- |
| `/`      | Home page (simple landing or redirect)         |
| `/add`   | Form page to submit a new café                 |
| `/cafes` | Displays all submitted cafés in a table format |

---

## 💡 Key Features

* 📝 WTForms-powered form for input validation and user-friendly experience
* 📍 Location field accepts only valid Google Maps URLs
* 📊 All cafés stored in a **CSV file**
* 🔗 Location displayed as clickable "Maps Link" in the table
* 🎨 Responsive UI styled with **Flask-Bootstrap 5**
* ✅ Client-side and server-side form validation

---

## 📁 Project Structure

```
Day62_CafeWifi/
├── main.py
├── templates/
│   ├── base.html
│   ├── add.html
│   ├── cafes.html
├── static/
│   └── (Optional CSS or image assets)
├── cafe-data.csv
```

---

## ⚙️ How to Use

1. **Clone the repo or download the files:**

   ```bash
   git clone https://github.com/yourusername/100-python-projects.git
   cd Day62_CafeWifi
   ```

2. **Install the required packages:**

   ```bash
   pip install flask flask-wtf flask-bootstrap
   ```

3. **Run the application:**

   ```bash
   python main.py
   ```

4. **Interact through the browser:**

   ```
   http://127.0.0.1:5000/add
   ```

---

## 🧰 Technologies Used

* Flask (Python Web Framework)
* Flask-WTF (Form handling and CSRF protection)
* Flask-Bootstrap (Easy Bootstrap integration)
* WTForms
* HTML5 & Jinja2 Templating
* CSV for lightweight data storage

---

## 🧠 What I Learned

* Creating and validating web forms using Flask-WTF
* Handling CSV read/write operations with UTF-8 encoding
* Dynamically rendering tables in HTML using Jinja2
* Making links clickable conditionally within templates
* Using Bootstrap for responsive form and table styling

---

✨ Find your next favorite work café — or help others find theirs!
