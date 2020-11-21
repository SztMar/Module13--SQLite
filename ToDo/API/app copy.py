from flask import Flask, jsonify, abort
from models import books


app = Flask(__name__)
app.config["SECRET_KEY"] = "MySecretKey"

@app.route("/api/v1/storage/", methods=["GET"])
def get_books():
    return jsonify(books.all())

@app.route("/api/v1/storage/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = books.get(book_id)
    if not book:
        abort(404)
    return jsonify({"book":book})
    



if __name__ == "__main__":
   app.run(debug=False)


