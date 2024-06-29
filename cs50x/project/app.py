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
    feed = None

    if client == "user":
        if client_name != session["user_name"]:
            header = db.execute("SELECT username AS name, photo FROM users WHERE username = ?", client_name)
        posts = db.execute("""SELECT post, blog_posts.id AS id, blog_posts.creation_time, group_name, user_name, photo FROM blog_posts
                            INNER JOIN groups on groupname = group_name WHERE user_name = ? OR group_name IN (?)
                            UNION SELECT post, blog_posts.id AS id, blog_posts.creation_time, group_name, user_name AS name, photo FROM blog_posts
                            INNER JOIN users on username = user_name WHERE user_name = ? and group_name is null ORDER BY blog_posts.creation_time DESC""", client_name, [group["groupname"] for group in session["user_groups"]], client_name)

    if client == "group":
        feed = client_name
        header = db.execute("SELECT groupname AS name, photo, accessibility FROM groups WHERE groupname = ?", client_name)
        if header[0]["name"] in [group["groupname"] for group in session["user_groups"]]:
            header[0]["is_member"] = "true"
        else:
            header[0]["is_member"] = "false"
        posts = db.execute("""SELECT post, blog_posts.id AS id, blog_posts.creation_time, user_name, photo FROM blog_posts
                           INNER JOIN users on username = user_name WHERE group_name = ? ORDER BY blog_posts.creation_time DESC""", client_name)

    return render_template("index.html", posts=posts, header=header, feed=feed)


@app.route("/submit/<type>", methods=["GET", "POST"])
@login_required
def post(type):

    data = None
    posts = None

    if request.method == "POST":

        if request.get_json():
            data = request.get_json()

        else:
            return "Failed to get input.", 400

        if not data["post-body"]:
            return "Please fill out the post body", 400

        db.execute("INSERT INTO blog_posts(user_name, post, group_name) VALUES(?,?,?)",
                    session["user_id"], data["post-body"], data["group_name"])

    else:
        if not request.args.get('id'):
            return "Could not parse request", 400
        else:
            post = db.execute("SELECT * FROM blog_posts WHERE id = ?", request.args.get('id'))

            if not post[0]:
                return "Could not find post", 400

            comments = db.execute("SELECT * FROM blog_posts INNER JOIN comments ON post = id WHERE id = ?", request.args.get('id'))
            return render_template("post.html", post=post, comments=comments)



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

        logging.warning([sess for sess in session["user_groups"] if sess["groupname"] == group[0]["groupname"]][0])

        try:
            db.execute("BEGIN")
            db.execute("INSERT INTO users_groups(user_name, group_name) VALUES(?,?)", session["user_name"], group_name)
            session["user_groups"].append({group[0]["groupname"], group[0]["photo"]})
            db.execute("COMMIT")
        except(ValueError):
            db.execute("ROLLBACK")
            db.execute("BEGIN")
            db.execute("DELETE FROM users_groups WHERE user_name = ? AND group_name = ?", session["user_name"], group_name)
            session["user_groups"].remove([x for x in session["user_groups"] if x["groupname"] == group[0]["groupname"]][0])
            db.execute("COMMIT")
            if group[0]["accessibility"] == "private":
                logging.warning("gothere")
                return redirect(f"/feed/user/{session["user_name"]}")


        return redirect(f"/feed/group/{group_name}")


@app.route("/groups")
@login_required
def groups():

        # db.execute("BEGIN")
        # groups = db.execute("SELECT groupname AS name, photo FROM groups WHERE accessibility = 'public'")
        # for group in groups:
        #     group_members = db.execute("SELECT COUNT(*) AS members FROM users_groups WHERE group_name = ?", group["name"])
        #     group["members"] = group_members[0]["members"]
        #     group_posts = db.execute("SELECT COUNT(*) AS posts FROM blog_posts WHERE group_name = ?", group["name"])
        #     group["posts"] = group_posts[0]["posts"]

        groups = db.execute("""SELECT DISTINCT groupname AS name, photo,
                            (SELECT COUNT(*) FROM users_groups WHERE group_name = groupname) AS members,
                            (SELECT COUNT(*) FROM blog_posts WHERE group_name = groupname) AS posts
                            FROM groups LEFT JOIN users_groups on groups.groupname = users_groups.group_name
                            LEFT JOIN blog_posts on groups.groupname = blog_posts.group_name
                            WHERE accessibility = 'public'""")

        return render_template("groups.html", groups=groups)


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
                "SELECT groupname, photo FROM groups INNER JOIN users_groups on groups.groupname = users_groups.group_name WHERE users_groups.user_name = ? ORDER BY users_groups.creation_time DESC", session["user_name"])

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
