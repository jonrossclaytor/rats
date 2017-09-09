from flask import Flask
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(port=5000, debug=True)
