from flask import Flask
from flask.ext.login import LoginManager
from flask.ext.login import login_required
from flask.ext.login import login_user
from flask.ext.login import logout_user
from flask.ext.login import current_user
from flask import render_template
from flask import redirect
from flask import request
from flask import url_for

app = Flask(__name__)
login_manager = LoginManager(app)

@app.route("/")
def home():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(port=5000, debug=True)
