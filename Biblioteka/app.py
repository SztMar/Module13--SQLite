from flask import Flask, redirect, render_template, request, url_for
from form import StorageForm
from models import books


app = Flask(__name__)
app.config["SECRET_KEY"] = "MySecretKey"

@app.route("/storage/", methods=["GET", "POST"])
def books_list():
    form = StorageForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            books.create(form.data)
            books.save_all()
        return redirect(url_for("books_list"))

    return render_template("form.html", form=form, books=books.all(), error=error)

@app.route("/storage/<int:task_id>/", methods=["GET", "POST"])
def books_details(task_id):
    task = books.get(task_id - 1)
    form = StorageForm(data=task)

    if request.method == "POST":
        if form.validate_on_submit():
            books.remove(task_id - 1)
        return redirect(url_for("books_details"))
    return render_template("form_id.html", form=form, task_id=task_id)


if __name__ == "__main__":
   app.run(debug=False)