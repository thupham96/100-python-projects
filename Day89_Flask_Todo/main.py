from flask import Flask, render_template, request, redirect, url_for, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    done = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<Task {self.id} {self.title[:20]!r}>"

def init_db():
    with app.app_context():
        if not os.path.exists("todo.db"):
            db.create_all()

@app.get("/")
def index():
    tasks = Task.query.order_by(Task.created_at.desc()).all()
    return render_template("index.html", tasks=tasks)

@app.post("/add")
def add_task():
    title = request.form.get("title", "").strip()
    if not title:
        return redirect(url_for("index"))
    db.session.add((Task(title=title)))
    db.session.commit()
    return redirect(url_for("index"))

@app.post("/toggle/<int:task_id>")
def toggle_task(task_id):
    task = Task.query.get_or_404(task_id)
    task.done = not task.done
    db.session.commit()
    return redirect(url_for("index"))

@app.get("/edit/<int:task_id>")
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    return render_template("edit.html", task=task)

@app.post("/edit/<int:task_id>")
def update_task(task_id):
    task = Task.query.get_or_404(task_id)
    title = request.form.get("title", "").strip()
    if not title:
        return redirect(url_for("index"))
    task.title = title
    db.session.commit()
    return redirect(url_for("index"))

@app.post("/delete/<int:task_id>")
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("index"))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
