from flask import Blueprint, Flask, render_template

views = Blueprint('views', __name__)


@views.route('/', endpoint='home')
def home():
    name = "homes"
    return render_template("home.html", name=name)