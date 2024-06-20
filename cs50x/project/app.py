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


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    if request.method == "GET":
        return render_template("buy.html")

    else:
        if not request.form.get("symbol"):
            return apology("must provide symbol")

        try:
            int(request.form.get("shares"))
        except ValueError:
            return apology("invalid shares")

        if not request.form.get("shares") or not int(request.form.get("shares")) > 0:
            return apology("invalid number of shares")

        quote = lookup(request.form.get("symbol"))

        if quote == None:
            return apology("invalid symbol")

        user_cash = db.execute(
            "SELECT cash FROM users where id = ?", session["user_id"]
        )

        cost = quote["price"] * int(request.form.get("shares"))

        if cost > user_cash[0]["cash"]:
            return apology("you do not have enough cash")

        else:
            logging.warning(user_cash[0]["cash"])
            logging.warning(cost)
            user_cash[0]["cash"] -= cost
            logging.warning(user_cash[0]["cash"])
            try:
                db.execute(
                    "INSERT INTO users_shares (user_id, symbol, shares) VALUES(?,?,?)",
                    session["user_id"],
                    request.form.get("symbol").upper(),
                    request.form.get("shares"),
                )
                logging.warning("Inserted first time")
            except ValueError:
                logging.warning("Already exist updating")
                shares = db.execute(
                    "SELECT shares FROM users_shares WHERE user_id = ? AND symbol = ?",
                    session["user_id"],
                    request.form.get("symbol").upper(),
                )
                shares[0]["shares"] += int(request.form.get("shares"))
                db.execute(
                    "UPDATE users_shares SET shares = ?, last_modified_date = ? WHERE user_id = ? AND symbol = ?",
                    shares[0]["shares"],
                    datetime.datetime.now(),
                    session["user_id"],
                    request.form.get("symbol").upper(),
                )
            db.execute(
                "INSERT INTO users_transaction_history (user_id, symbol, shares, action) VALUES(?,?,?,?)",
                session["user_id"],
                request.form.get("symbol").upper(),
                request.form.get("shares"),
                "buy",
            )
            db.execute(
                "UPDATE users SET cash = ? WHERE id = ?",
                user_cash[0]["cash"],
                session["user_id"],
            )
            flash("Purchase Successful")
            return redirect("/")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    users_transaction_history = db.execute(
        "SELECT * FROM users_transaction_history WHERE user_id = ?", session["user_id"]
    )
    history = []
    for i in range(len(users_transaction_history)):
        price = lookup(users_transaction_history[i]["symbol"])
        color = ""
        action = ""
        if users_transaction_history[i]["action"] == "sell":
            color = "red"
            action = "SOLD"
        else:
            color = "green"
            action = "BOUGHT"
        history.append(
            {
                "symbol": users_transaction_history[i]["symbol"],
                "shares": users_transaction_history[i]["shares"],
                "price": price["price"],
                "transaction": action,
                "date": users_transaction_history[i]["creation_date"],
                "color": color,
            }
        )
    return render_template("history.html", history=history)


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
        flash("Login Successful")
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
            return render_template(
                "quoted.html", symbol=quote["symbol"], price=quote["price"]
            )


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Ensure password confirmation was submitted
        elif not request.form.get("confirmation"):
            return apology("must provide password confimation", 400)

        # Ensure password confirmation is correct
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("your password did not match", 400)

        # Hash password
        password_hash = generate_password_hash(request.form.get("password"))

        # Insert into do
        try:
            db.execute(
                "INSERT INTO users (username, hash) VALUES(?,?)",
                request.form.get("username"),
                password_hash,
            )
        except ValueError:
            return apology("username taken", 400)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        flash("Registration Successful")
        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        symbols = db.execute(
            "SELECT symbol FROM users_shares WHERE user_id = ?", session["user_id"]
        )
        return render_template("sell.html", symbols=symbols)

    else:
        if not request.form.get("symbol"):
            return apology("must provide symbol")

        shares = db.execute(
            "SELECT * FROM users_shares WHERE user_id = ? AND symbol = ?",
            session["user_id"],
            request.form.get("symbol").upper(),
        )

        cash = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])

        absShares = abs(int(request.form.get("shares")))

        if not request.form.get("shares") or absShares > shares[0]["shares"]:
            return apology("invalid/not enough number of shares")

        shares[0]["shares"] -= absShares

        price = lookup(request.form.get("symbol"))
        cash[0]["cash"] += price["price"] * absShares

        if shares[0]["shares"] == 0:
            db.execute(
                "DELETE FROM users_shares WHERE user_id = ? AND symbol = ?",
                session["user_id"],
                request.form.get("symbol").upper(),
            )

        db.execute(
            "UPDATE users_shares SET shares = ?, last_modified_date = ? WHERE user_id = ? AND symbol = ?",
            shares[0]["shares"],
            datetime.datetime.now(),
            session["user_id"],
            request.form.get("symbol").upper(),
        )
        db.execute(
            "INSERT INTO users_transaction_history (user_id, symbol, shares, action) VALUES(?,?,?,?)",
            session["user_id"],
            request.form.get("symbol").upper(),
            -abs(int(request.form.get("shares"))),
            "sell",
        )
        db.execute(
            "UPDATE users SET cash = ? WHERE id = ?",
            cash[0]["cash"],
            session["user_id"],
        )
        flash("Successfull sold")
        return redirect("/")


@app.route("/change-password", methods=["GET", "POST"])
@login_required
def changePassword():
    """Change Password"""

    if request.method == "GET":
        return render_template("change-password.html")

    else:
        if not request.form.get("old_password") or not request.form.get("new_password"):
            return apology("must provide password", 403)

        elif not request.form.get("confirmation"):
            return apology("must provide password confimation", 403)

        elif request.form.get("new_password") != request.form.get("confirmation"):
            return apology("your password did not match", 403)

        rows = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])

        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("old_password")
        ):
            return apology("incorrect password", 403)

        password_hash = generate_password_hash(request.form.get("new_password"))

        db.execute(
            "UPDATE users SET hash = ? WHERE id = ?", password_hash, session["user_id"]
        )

        flash("Password changed successfully")
        return redirect("/")


@app.route("/settings")
@login_required
def settings():
    return render_template("settings.html")


@app.route("/cash", methods=["GET", "POST"])
@login_required
def cash():
    if request.method == "GET":
        return render_template("cash.html")

    else:
        if not request.form.get("cash"):
            return apology("must provide amount")

        user = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])

        user[0]["cash"] += int(request.form.get("cash"))

        db.execute(
            "UPDATE users SET cash = ? WHERE id = ?",
            user[0]["cash"],
            session["user_id"],
        )

        flash("Cash acquired")
        return redirect("/")


@app.route("/buy_or_sell", methods=["POST"])
@login_required
def buy_or_sell():

    if not request.form.get("shares") or int(request.form.get("shares")) == 0:
        return apology("must provide amount")

    if int(request.form.get("shares")) > 0:
        return buy()

    if int(request.form.get("shares")) < 0:
        return sell()
