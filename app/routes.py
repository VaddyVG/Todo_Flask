from app.models import Todo
from flask import render_template, redirect, request, url_for, Blueprint
from app import db


main_bp = Blueprint("main", __name__)

@main_bp.route("/")
def get_todo():
    """Функция, возвращающая весь список дел."""
    todo_list = Todo.query.order_by(Todo.id).all()
    return render_template("base.html", todo_list=todo_list)


@main_bp.route("/add", methods=["POST"])
def add():
    """Добавление записи в список дел."""
    title = request.form.get("title")
    if not title or len(title.strip()) == 0:
        return redirect(url_for("main.get_todo"))
    new_todo = Todo(title=title)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("main.get_todo"))


@main_bp.route("/update/<int:todo_id>", methods=["POST"])
def update(todo_id: int):
    """Обновление состояние дела (Not complete; Completed)."""
    todo = Todo.query.get_or_404(todo_id)
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for("main.get_todo"))


@main_bp.route("/delete/<int:todo_id>", methods=["POST"])
def delete(todo_id):
    """Удаление записи из списка дел."""
    todo = Todo.query.get_or_404(todo_id)
    if todo:
        db.session.delete(todo)
        db.session.commit()
    return redirect(url_for("main.get_todo"))
