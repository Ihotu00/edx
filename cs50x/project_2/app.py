import os
import logging
from datetime import datetime, timedelta
import re
from uuid import uuid4

from cs50 import SQL
from flask import Flask, redirect, render_template, request, session
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
db = SQL("sqlite:///blog.db")


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

@app.template_filter('date')
def format_date(date):
    datetime_object = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    return datetime_object.strftime("%b %d, %Y")

@app.template_filter('time')
def format_time(date):
    datetime_object = datetime.strptime(date, '%Y-%m-%d %H:%M:%S')
    return datetime_object.strftime("%H:%M")


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

    followingList = [following["user"] for following in session["user_following"]]
    followingList.append(session["user_name"])
    logging.warning(followingList)

    posts = db.execute("""SELECT post, posts.id AS id, posts.creation_time, created_by, photo, title, rating FROM posts
                        INNER JOIN users on username = created_by WHERE created_by IN (?) AND type != 'comment_post'
                        ORDER BY posts.creation_time DESC""",
                        followingList)

    return render_template("index.html", posts=posts)



@app.route("/post")
@app.route("/post/submit", methods=["POST"])
@login_required
def post():
    if request.method == "POST":

            if request.get_json():
                data = request.get_json()

            else:
                return "Failed to get input.", 400

            if not data["post_body"]:
                return "Please fill out the post body", 400
            if not data["type"]:
                return "Couldn't parse type", 400

            id = f"{uuid4()}"
            db.execute("BEGIN")
            db.execute("INSERT INTO posts(id, created_by, post, type) VALUES(?,?,?,?)",
                        id, session["user_name"], data["post_body"], data["type"])

            if data["type"] == "comment_post":
                if not request.args.get('id'):
                    return "Could not parse request", 400

                og_post = db.execute("SELECT * FROM posts WHERE id = ?", request.args.get('id'))
                if not og_post:
                    return "Could not find post", 400

                db.execute("INSERT INTO comments(post_id, comment_id) VALUES(?,?)", request.args.get('id'), id)
                db.execute("COMMIT")
                return f"{request.args.get('id')}", 200

            else:
                db.execute("COMMIT")
                return f"{id}", 200

    else:
        post = db.execute("""SELECT posts.id, posts.created_by, post, posts.creation_time AS creation_time, photo,
                          (SELECT COUNT(*) FROM comments WHERE post_id = posts.id) AS comments_count FROM posts
                          INNER JOIN users on username = created_by WHERE posts.id = ?""", request.args.get('id'))

        if not post:
            return "Could not find post", 400

        comments = db.execute("SELECT *, (SELECT COUNT(*)) AS count FROM posts INNER JOIN comments ON comment_id = id WHERE post_id = ?", request.args.get('id'))

        for comment in comments:
            comment["photo"] = (db.execute("SELECT photo FROM users WHERE username = ?", comment["created_by"]))[0]["photo"]
        return render_template("post.html", post=post[0], comments=comments)


@app.route("/follow/<username>", methods=["POST"])
@login_required
def follow(username):

    if username:

        user = db.execute(
            "SELECT * FROM users WHERE username = ?", username)

        if not user:
            return "Could not find user", 400

        try:
            db.execute("BEGIN")
            db.execute("INSERT INTO users_followers(user, follower) VALUES(?,?)", username, session["user_name"])
            session["user_groups"].append({"user": user[0]["username"], "photo": user[0]["photo"]})
            db.execute("COMMIT")
        except(ValueError):
            db.execute("ROLLBACK")
            db.execute("BEGIN")
            db.execute("DELETE FROM users_followers WHERE user = ? AND follower = ?", username, session["user_name"])
            session["user_following"].remove([x for x in session["user_following"] if x["user"] == user[0]["username"]][0])
            db.execute("COMMIT")

        return redirect(f"/feed/{username}")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    session.clear()

    if request.method == "POST":
        if request.get_json():
            data = request.get_json()

            if not data["username"]:
                return "Please provide Username", 400

            elif not data["password"]:
                return "Please provide Password", 400

            rows = db.execute(
                "SELECT * FROM users WHERE username = ?",  data["username"]
            )

            if len(rows) != 1 or not check_password_hash(
                rows[0]["password"],  data["password"]
            ):
                return "Invalid username/password", 400

            session["user_id"] = rows[0]["id"]
            session["user_photo"] = rows[0]["photo"]
            session["user_name"] = rows[0]["username"]
            session["user_following"] = db.execute(
                """SELECT user, photo FROM users INNER JOIN users_followers on username = user WHERE follower = ?
                ORDER BY users_followers.creation_time DESC""", session["user_name"])
            session["user_followers"] = db.execute(
                """SELECT follower, photo FROM users INNER JOIN users_followers on username = follower WHERE user = ?
                ORDER BY users_followers.creation_time DESC""", session["user_name"])

            return "Login Successful", 200

        else:
            return "invalid json", 400

    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    session.clear()

    return redirect("/login")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    session.clear()

    if request.method == "POST":

        if request.get_json():
            data = request.get_json()

            if not data["username"]:
                return "Please provide Username", 400

            elif not data["password"]:
                return "Please provide Password", 400

            elif not data["confirmation"]:
                return "Please confirm Password", 400

            elif data["password"] != data["confirmation"]:
                return "Passwords do not match", 400

            elif not data["photo"]:
                return "Photo is null", 400

            password_hash = generate_password_hash(data["password"])
            id = f"{uuid4()}"

            try:
                db.execute(
                    "INSERT INTO users (id, username, password, photo) VALUES(?,?,?, ?)",
                    id,
                    data["username"],
                    password_hash,
                    data["photo"]
                )
            except ValueError:
                return "Username taken", 400

            rows = db.execute(
                "SELECT * FROM users WHERE username = ?", data["username"]
            )

            session["user_id"] = rows[0]["id"]
            session["user_photo"] = rows[0]["photo"]
            session["user_name"] = rows[0]["username"]

            return "Registration Successful", 200

    else:
        return render_template("register.html")