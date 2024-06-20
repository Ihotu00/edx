import os
import logging
import datetime

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from functools import wraps
from werkzeug.security import check_password_hash, generate_password_hash


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

    posts = db.execute("SELECT * FROM blog_posts WHERE user_id = ? ORDER BY creation_time DESC", session["user_id"])

    groups = db.execute("SELECT * FROM groups left join users_groups on groups.id = users_groups.group_id WHERE user_id = ?", session["user_id"])
    """select movies.title
from movies
left join ratings
on movies.id = ratings.movie_id
where id in(
    select movie_id
    from stars
    where person_id =(
        select id
        from people
        where name = "Chadwick Boseman"
    )
)"""
    logging.warning(groups)

    return render_template("index.html", posts=posts)


@app.route("/post", methods=["POST"])
@login_required
def post():
    """Show portfolio of stocks"""

    group_id = None

    if request.form.get("group_id") and int(request.form.get("group_id")):
        group_id = int(request.form.get("group_id"))

    if request.form.get("message"):
        db.execute("INSERT INTO blog_posts(user_id, post, group_id) VALUES(?,?,?)", session["user_id"], request.form.get("message"), group_id)
    return redirect("/")


@app.route("/create/group", methods=["POST"])
@login_required
def create_group():
    """Show portfolio of stocks"""

    if request.form.get("group_name"):
        try:
            db.execute("INSERT INTO groups(created_by, group_name) VALUES(?,?)", session["user_id"], request.form.get("group_name"))
        except (ValueError):
            flash("Sorry that name is unavailbale. Try something else")
            return redirect("/")

        group = db.execute("SELECT * FROM groups WHERE group_name = ?", request.form.get("group_name"))
        db.execute("INSERT INTO users_groups(user_id, group_id) VALUES(?,?)", session["user_id"], group[0]["id"])
        flash("Created Successfully")
    return redirect("/")



@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            flash("Please provide Username")
            return render_template("login.html")

        # Ensure password was submitted
        elif not request.form.get("password"):
            flash("Please provide Password")
            return render_template("login.html")

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["password"], request.form.get("password")
        ):
            ("Invalid username/password")
            return render_template("login.html")

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
    return redirect("/login")



@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Forget any user_id
    session.clear()

    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            flash("Please provide Username")
            return render_template("register.html")

        # Ensure password was submitted
        elif not request.form.get("password"):
            flash("Please provide Password")
            return render_template("register.html")

        # Ensure password confirmation was submitted
        elif not request.form.get("confirmation"):
            flash("Please confirm Password")
            return render_template("register.html")

        # Ensure password confirmation is correct
        elif request.form.get("password") != request.form.get("confirmation"):
            flash("Passwords do not match")
            return render_template("register.html")

        # Hash password
        password_hash = generate_password_hash(request.form.get("password"))

        # Insert into do
        try:
            db.execute(
                "INSERT INTO users (username, password) VALUES(?,?)",
                request.form.get("username"),
                password_hash,
            )
        except ValueError:
            flash("Username taken")
            return render_template("register.html")

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
