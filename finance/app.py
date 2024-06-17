import os
import logging
import datetime

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


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
    user_shares = db.execute("SELECT * FROM users_shares WHERE user_id = ?", session["user_id"])
    user = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
    user_data = []
    total = 0
    for i in range(len(user_shares)):
        price = lookup(user_shares[i]["symbol"])
        user_data.append({'symbol': user_shares[i]["symbol"],
                          'shares': user_shares[i]["shares"],
                          'price': price["price"],
                          'worth': int(user_shares[i]["shares"]) * price["price"]
                          })
    for i in range(len(user_data)):
        total += float(user_data[i]["worth"])
    total += user[0]["cash"]
    return render_template("index.html", user_data=user_data, cash=user[0]["cash"], total=total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "GET":
        return render_template("buy.html")

    else:
        if not request.form.get("symbol"):
            return apology("must provide symbol")

        if not request.form.get("shares") or not int(request.form.get("shares")) > 0:
            return apology("invalid number of shares")

        quote = lookup(request.form.get("symbol"))

        if quote == None:
            return apology("invalid symbol")

        user_cash = db.execute("SELECT cash FROM users where id = ?", session["user_id"])

        cost = quote["price"] * int(request.form.get("shares"))

        if cost > user_cash[0]["cash"]:
            return apology("you do not have enough cash")

        else:
            logging.warning(user_cash[0]["cash"])
            logging.warning(cost)
            user_cash[0]["cash"] -= cost
            logging.warning(user_cash[0]["cash"])
            try:
                db.execute("INSERT INTO users_shares (user_id, symbol, shares) VALUES(?,?,?)",
                       session["user_id"], request.form.get("symbol"), request.form.get("shares"))
                logging.warning("Inserted first time")
            except(ValueError):
                logging.warning("Already exist updating")
                shares = db.execute("SELECT shares FROM users_shares WHERE user_id = ? AND symbol = ?",
                                           session["user_id"], request.form.get("symbol"))
                shares[0]["shares"] += int(request.form.get("shares"))
                db.execute("UPDATE users_shares SET shares = ?, last_modified_date = ? WHERE user_id = ? AND symbol = ?",
                                         shares[0]["shares"], datetime.datetime.now(), session["user_id"], request.form.get("symbol"))
            db.execute("INSERT INTO users_transaction_history (user_id, symbol, shares, action) VALUES(?,?,?,?)",
                       session["user_id"], request.form.get("symbol"), request.form.get("shares"), "buy")
            db.execute("UPDATE users SET cash = ? WHERE id = ?", user_cash[0]["cash"], session["user_id"])
            return redirect("/")



@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "GET":
        return render_template("quote.html")

    else:
        if not request.form.get("symbol"):
            return apology("must provide symbol")

        quote = lookup(request.form.get("symbol"))

        if quote == None:
            return apology("invalid symbol")

        else:
            return render_template("quoted.html", symbol=quote["symbol"], price=quote["price"])


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("name"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Ensure password confirmation was submitted
        elif not request.form.get("confirmation"):
            return apology("must provide password confimation", 403)

        # Ensure password confirmation is correct
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("your password did not match", 403)

        # Hash password
        password_hash = generate_password_hash(request.form.get("password"))

        # Insert into do
        try:
            db.execute(
                "INSERT INTO users (username, hash) VALUES(?,?)", request.form.get("name"), password_hash
                )
        except(ValueError): return apology("username taken", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("name")
        )

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        symbols = db.execute("SELECT symbol, shares FROM users_shares WHERE user_id = ?", session["user_id"])
        logging.warning(symbols)
        return render_template("sell.html", symbols=symbols)

    else:
        
