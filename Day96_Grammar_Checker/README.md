# Day 96: Grammar Checker – Flask + LanguageTool API

A simple yet powerful web-based grammar checker built with **Flask** that integrates with the [LanguageTool API](https://languagetool.org/http-api/swagger-ui/#/) to detect and suggest corrections for grammar, spelling, and style issues.

---

## Features

* Clean web interface for inputting and analyzing text
* Integration with LanguageTool API for real-time grammar suggestions
* Highlights grammar issues and provides correction suggestions
* Auto-generates corrected version of the text
* Displays both original and corrected text side-by-side
* Handles API errors and invalid responses gracefully

---

## Technologies Used

* Python 3
* Flask – lightweight web framework
* requests – for API calls
* HTML + Jinja2 – for rendering templates
* LanguageTool API – for grammar and spelling checks

---

## Project Structure

```
.
├── app.py             # Main Flask app with routing and logic
└── templates/
    ├── index.html     # Input form for text
    └── result.html    # Output results: suggestions and corrected text
```

---

## How to Run

1. Install dependencies:

   ```bash
   pip install flask requests
   ```

2. Clone or download the project:

   ```bash
   git clone https://github.com/thupham96/100-python-projects.git
   cd Day96_Grammar_Checker
   ```

3. Run the app:

   ```bash
   python app.py
   ```

4. Open your browser and visit:

   ```
   http://127.0.0.1:5000/
   ```

---

## How to Use

1. Enter your English text in the input box.
2. Click "Check Grammar".
3. View detected issues and suggestions.
4. See the corrected text below the original.

---

## What I Learned

* Using external APIs (LanguageTool) within Flask apps
* Sorting and applying offset-based corrections to a string
* Handling form submission and API responses in Flask
* Creating dynamic, user-friendly HTML templates with Jinja2
* Managing string manipulation and error handling in web apps
