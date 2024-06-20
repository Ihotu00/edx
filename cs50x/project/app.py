import os
import logging
import datetime

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from functools import wraps


# Configure application
app = Flask(__name__)


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///tunglr.db")

def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/latest/patterns/viewdecorators/
    """

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)

    return decorated_function

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()
    user_shares = db.execute(
        "SELECT * FROM users_shares WHERE user_id = ?", session["user_id"]
    )
    user = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
    user_data = []
    total = 0
    for i in range(len(user_shares)):
        price = lookup(user_shares[i]["symbol"])
        user_data.append(
            {
                "symbol": user_shares[i]["symbol"],
                "shares": user_shares[i]["shares"],
                "price": price["price"],
                "worth": int(user_shares[i]["shares"]) * price["price"],
            }
        )
    for i in range(len(user_data)):
        total += float(user_data[i]["worth"])
    total += user[0]["cash"]
    return render_template(
        "index.html", user_data=user_data, cash=user[0]["cash"], total=total
    )

    return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/login")



@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Forget any user_id
    session.clear()

    return render_template("register.html")
