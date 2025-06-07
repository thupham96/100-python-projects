# Day 57: 📝 Blog Viewer App – Flask + JSON API with Search 🔍

A Flask web app that fetches blog content from a remote JSON API and displays individual posts. Includes a simple full-text search to filter posts by title or subtitle.

---

## 📖 Overview

**Blog Viewer App** is a Flask project that:

* Retrieves blog post data from a hosted JSON API
* Displays a homepage with all blog post summaries
* Allows users to click into individual blog posts
* Supports keyword-based search to filter content

---

## 🚀 How to Run

```bash
python main.py
```

Then open your browser at:

```
http://127.0.0.1:5000/
```

Try searching with:

```
http://127.0.0.1:5000/search?query=python
```

---

## 🗺️ Routes & Features

| Route               | Description                                                                 |
| ------------------- | --------------------------------------------------------------------------- |
| `/`                 | Homepage listing all blog posts                                             |
| `/post/<int:index>` | Detailed page for individual post based on its ID                           |
| `/search?query=...` | Filters and displays posts that match the search query in title or subtitle |

---

## 💡 Key Features

* 📡 Data pulled dynamically from an external **JSON API**
* 🔍 Real-time post filtering via query parameter search
* 🧭 Dynamic routing using `/<int:index>` URL structure
* 🎨 Clean HTML layout with custom CSS and Google Fonts
* 🖥️ Lightweight and responsive frontend design

---

## 📁 Project Structure

```
Day57_BlogViewer/
├── main.py
├── post.py
├── templates/
│   ├── index.html
│   └── post.html
├── static/
│   └── css/
│       └── styles.css
```

---

## 🧰 Technologies Used

* Flask (Python Web Framework)
* Jinja2 for HTML templating
* `requests` for HTTP API fetching
* HTML5 + CSS3 for frontend structure and styling

---

## 🧠 What I Learned

* How to fetch and render external JSON data in Flask
* Dynamic URL routing and parameter handling in Flask
* Implementing basic search functionality with list comprehensions
* Structuring multi-template Flask apps with shared data

---

📰 Browse, read, and search posts from a JSON-powered blog interface — all served dynamically through Flask!
