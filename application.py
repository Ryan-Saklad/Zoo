from cs50 import SQL
from flask import Flask, render_template, request


app = Flask(__name__)
db = SQL("sqlite:///zoo.db")


@app.route("/")
def home():
    animals = db.execute("SELECT * FROM animals")
    return render_template("home.html", animals=animals)


@app.route("/search", methods=["GET", "POST"])
def search():
    if request.method == "GET":
        return render_template("search.html")
    else:
        return render_template("results.html")


if __name__ == "__main__":
    app.run()
