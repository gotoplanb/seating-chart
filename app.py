import json
from flask import Flask, render_template

app = Flask(__name__)


def load_guests():
    with open("data.json") as f:
        return json.load(f)


@app.route("/")
def index():
    guests = load_guests()
    return render_template("index.html", guests=guests)


if __name__ == "__main__":
    app.run(debug=True)
