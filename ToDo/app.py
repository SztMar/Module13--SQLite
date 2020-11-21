from flask import Flask, request, render_template, redirect, url_for

from form import TodoForm
from models import todos
import sqlite3 
import views

app = Flask(__name__)


app.config["SECRET_KEY"] = "nininini"

@app.route("/todos/", methods=["GET", "POST"])
def todos_list():
    form = TodoForm()
    error = ""
    todos.__init__()
    if request.method == "POST":
        if form.validate_on_submit():
            todos.add_record(form.data)            
            
        return redirect(url_for("todos_list"))

    return render_template("todos.html", form=form, todos=todos.select_all(), error=error)


@app.route("/todos/<int:Key>/", methods=["GET", "POST"])
def todo_details(Key):
    todo = todos.get_key(Key - 1)    
    form = TodoForm(data=todo)
    

    if request.method == "POST":
        if form.validate_on_submit():
            todos.update_record(Key - 1, form.data)
        return redirect(url_for("todos_list"))
    return render_template("todo.html", form=form, Key=Key)

@app.route("/todos/delete/")
def delete_list():
    todos.__init__()
    
    return render_template("delete_list.html", todos=todos.select_all())

@app.route("/todos/delete/<int:Key>/", methods=["GET", "POST"])
def delete_details(Key):
    delete = todos.get_key(Key - 1)    
    form = TodoForm(data=delete)
    

    if request.method == "POST":
        if form.validate_on_submit():
            todos.delete_record(Key - 1, form.data)
        return redirect(url_for("delete_list"))
    return render_template("delete.html", form=form, Key=Key)



if __name__ == "__main__":
    app.run(debug=True)

    conn = create_connection("ToDoDB.db")
    