from flask import render_template, request, url_for, redirect
from types import new_class
from application import app, db
from application.models import Tasks
from application.forms import TaskForm

@app.route('/')
def home():
    all_tasks = Tasks.query.all()
    return render_template("index.html", title="Home", all_tasks=all_tasks)

@app.route('/Create_task', methods=["GET", "POST"])
def create_task():
    form = TaskForm()
    if request.method == "POST":
        new_task = Tasks(description=form.description.data)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("create_task.html", title="Add a Task", form=form)