import os
import logging
import datetime
import re

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


@app.route("/feed/<client>/<client_name>")
@login_required
def index(client, client_name):

    header= None

    if client == "user":
        if client_name != session["user_name"]:
            header = db.execute("SELECT username AS name, photo FROM users WHERE username = ?", client_name)
        posts = db.execute("""SELECT post, blog_posts.id AS id, blog_posts.creation_time, group_name, user_name, photo FROM blog_posts
                            INNER JOIN groups on groupname = group_name WHERE user_name = ? OR group_name IN (?)
                            UNION SELECT post, blog_posts.id AS id, blog_posts.creation_time, group_name, user_name AS name, photo FROM blog_posts
                            INNER JOIN users on username = user_name WHERE user_name = ? and group_name is null ORDER BY blog_posts.creation_time DESC""", client_name, [group["groupname"] for group in session["user_groups"]], client_name)

    if client == "group":
        header = db.execute("SELECT groupname AS name, photo, accessibility FROM groups WHERE groupname = ?", client_name)
        if header[0]["name"] in [group["groupname"] for group in session["user_groups"]]:
            header[0]["is_member"] = "true"
        else:
            header[0]["is_member"] = "false"
        posts = db.execute("""SELECT post, blog_posts.id AS id, blog_posts.creation_time, user_name, photo FROM blog_posts
                           INNER JOIN users on username = user_name WHERE group_name = ? ORDER BY blog_posts.creation_time DESC""", client_name)
        # logging.warning(header[0]["is_member"])

    # logging.warning([sess["groupname"] for sess in session["user_groups"]])
    # logging.warning(posts)
    return render_template("index.html", posts=posts, header=header)


@app.route("/post/comments/<id>", methods=["POST"])
@login_required
def post(id):

    data = None
    group_id = None
    posts = None

    if request.method == "POST":

        if request.get_json():
            data = request.get_json()
            if data["group_id"]:
                group_id = data["group_id"]

        else:
            return "Failed to get input.", 200

        if not data["message"]:
            return "", 400

        db.execute("INSERT INTO blog_posts(user_id, post, group_id) VALUES(?,?,?)",
                   session["user_id"], data["message"], group_id)

        posts = db.execute(
            """SELECT post, blog_posts.id AS id, creation_time, username, photo FROM blog_posts
            INNER JOIN users on users.id = blog_posts.user_id WHERE user_id = ? ORDER BY creation_time DESC""", session["user_id"])

        # return render_template("post.html", post=post, comments=comments)


@app.route("/create/group", methods=["POST"])
@login_required
def create_group():

    if request.get_json():
        data = request.get_json()

        if not re.search("^[a-zA-Z]", data["group_name"]):
            return "Invalid Name", 404

        logging.warning(data)

        try:
            db.execute("INSERT INTO groups(created_by, groupname, photo, accessibility) VALUES(?,?,?,?)", session["user_name"], data["group_name"], data["group_photo"], data["access"])
        except (ValueError):
            return "Sorry that name is unavailbale. Try something else", 400

        db.execute("INSERT INTO users_groups(user_name, group_name) VALUES(?,?)", session["user_name"], data["group_name"])
        group = db.execute("SELECT * from groups WHERE groupname = ?", data["group_name"])
        session["user_groups"].append(group[0])

        return f"/feed/group/{data["group_name"]}", 200

    else: return "ERROR: Could not read data", 400


@app.route("/join/<group_name>", methods=["POST"])
@login_required
def join_group(group_name):

    if group_name:

        group = db.execute(
            "SELECT * FROM groups WHERE groupname = ?", group_name)

        try:
            db.execute("BEGIN")
            db.execute("INSERT INTO users_groups(user_name, group_name) VALUES(?,?)", session["user_name"], group_name)
            session["user_groups"].append(group[0])
            db.execute("COMMIT")
        except(ValueError):
            db.execute("ROLLBACK")
            db.execute("BEGIN")
            db.execute("DELETE FROM users_groups WHERE user_name = ? AND group_name = ?", session["user_name"], group_name)
            session["user_groups"].remove(group[0])
            db.execute("COMMIT")


        return redirect(f"/feed/group/{group_name}")


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
            session["user_groups"] = db.execute(
                "SELECT * FROM groups INNER JOIN users_groups on groups.groupname = users_groups.group_name WHERE users_groups.user_name = ? ORDER BY creation_time DESC", session["user_name"])

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

            try:
                db.execute(
                    "INSERT INTO users (username, password, photo) VALUES(?,?,?)",
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
