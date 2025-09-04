# Day 88: Cafe & Wifi – Flask Web App

This project builds on the **Cafe & Wifi API** (Day 66) and transforms it into a **fully interactive website**. It allows users to browse, search, add, update, and delete cafes — all backed by an SQLite database and a Flask web server.

---

## Features

* **Interactive Web Pages** for:

  * Viewing all cafes with filters (location, wifi, sockets, toilets, calls, seating)
  * Viewing detailed cafe pages
  * Adding new cafes through a form
  * Updating coffee prices
  * Deleting cafes (with admin key)
* **REST API Endpoints**:

  * `GET /all` – list all cafes in JSON
  * `GET /random` – fetch a random cafe
  * `GET /search?loc=...` – find cafes by location
  * `POST /add` – add new cafes (form or JSON)
  * `PATCH /update/<id>` – update a cafe’s coffee price
  * `DELETE /report-closed/<id>` – delete a cafe (API key required)
* **Database Integration**:

  * SQLite with SQLAlchemy ORM
  * Automatic table creation if missing
* **Flash Messages & Validation**
* **Reusable Templates** for consistency
* **Debug Endpoint** `/__dbinfo` to inspect DB setup

---

## Technologies Used

* **Python**
* **Flask** – for web server and routing
* **Flask-SQLAlchemy** – ORM for SQLite
* **HTML + Jinja2 templates** – for dynamic rendering
* **Bootstrap (optional)** – styling for forms and tables
* **random, re** – for choosing random cafes and seat filtering
* **Environment variables** – API key & DB path configuration

---

## How to Run

1. Clone the repository or copy the code:

   ```bash
   git clone https://github.com/thupham96/100-python-projects.git
   cd Day88_Cafe_Website
   ```

2. Install dependencies:

   ```bash
   pip install flask flask_sqlalchemy
   ```

3. Run the application:

   ```bash
   python main.py
   ```

4. Visit the app in your browser:

   ```
   http://127.0.0.1:5000/
   ```

---

## Example Usage

1. Navigate to **/cafes** to view all cafes.
2. Use filters like `?wifi=on&loc=London` to refine results.
3. Click on a cafe to view details.
4. Add new cafes via **/ui/add** form.
5. Update coffee prices from the cafe detail page.
6. Delete cafes via **/ui/delete/<id>** with the admin key.

---

## What I Learned

* Building a **full CRUD Flask app** with both UI and API.
* Using **SQLAlchemy ORM** to define models and interact with SQLite.
* Rendering templates with Jinja2 and handling user input via forms.
* Implementing secure delete operations with API keys.
* Designing REST API endpoints alongside a user-friendly web interface.
* Using flash messages for real-time feedback in the UI.
