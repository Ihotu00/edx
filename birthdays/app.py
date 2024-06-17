import os
import logging

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # TODO: Add the user's entry into the database

        if not request.form.get("name"):
            flash("Invalid Name")
            return redirect("/")

        if not request.form.get("date"):
            flash("Invalid Date")
            return redirect("/")

        month = request.form.get("date").split('-')[1].lstrip('0')
        day = request.form.get("date").split('-')[2].lstrip('0')

        db.execute("INSERT INTO birthdays (name, day, month) VALUES (?,?,?)", request.form.get("name"), day, month)
        flash("Added Successfully")

        return redirect("/")

    else:

        # TODO: Display the entries in the database on index.html

        birthdays = db.execute("SELECT * FROM birthdays")

        return render_template("index.html", birthdays=birthdays)


@app.route("/action", methods=["POST"])
def action():
    if request.form.get("delete"):
        db.execute("DELETE FROM birthdays where id = ?", request.form.get("delete"))
        flash("Deleted")
        return redirect("/")
