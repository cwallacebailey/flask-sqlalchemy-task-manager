""" a module """


from flask import render_template
from taskmanager import app, DB_URL

@app.route("/")
def home():
    return render_template("base.html")