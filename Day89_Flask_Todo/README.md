# Day 89: Flask To-Do List App

This project is a **simple task manager web app** built with **Flask** and **SQLite**. It allows users to add, edit, mark as complete, and delete tasks. The app uses **SQLAlchemy ORM** for database interactions and a clean, minimal **HTML/Jinja2 interface** for task management.

---

## Features

* **Task Management**

  * Add new tasks
  * Toggle completion (done/undone)
  * Edit existing tasks
  * Delete tasks
* **Database Integration**

  * SQLite with SQLAlchemy ORM
  * Auto-creates `todo.db` if missing
* **Task Ordering**

  * Most recently created tasks appear first
* **Simple UI**

  * Templates: `index.html` (task list) and `edit.html` (task editor)
* **Error Handling**

  * `get_or_404` for invalid task IDs
* **Clean Code Design**

  * `Task` model with `id`, `title`, `done`, and `created_at`

---

## Technologies Used

* **Python**
* **Flask** – lightweight web framework
* **Flask-SQLAlchemy** – ORM for SQLite
* **Jinja2** – HTML templating
* **Datetime** – task creation timestamps
* **OS** – check for existing DB

---

## How to Run

1. Clone or copy the project:

   ```bash
   git clone https://github.com/thupham96/100-python-projects.git
   cd Day89_Flask_Todo
   ```

2. Install dependencies:

   ```bash
   pip install flask flask_sqlalchemy
   ```

3. Run the app:

   ```bash
   python main.py
   ```

4. Open in browser:

   ```
   http://127.0.0.1:5000/
   ```

---

## Example Usage

1. Visit the homepage `/` to see the to-do list.
2. Add tasks via the **Add Task** form.
3. Click checkboxes to **toggle completion**.
4. Use **Edit** links to update task names.
5. Use **Delete** buttons to remove tasks.

---

## What I Learned

* Building a **CRUD Flask app** with SQLite and SQLAlchemy.
* Designing **task models** with timestamps and booleans.
* Using **Flask routes** with `GET`, `POST`, and `get_or_404`.
* Handling **form submissions** and redirects with `url_for`.
* Implementing **task toggling** and **edit functionality** cleanly.
* Keeping the UI simple but functional with Jinja2 templates.
