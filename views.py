from flask import Blueprint, render_template, request, jsonify, redirect, url_for

views = Blueprint(__name__, "views")

@views.route("/Home")
def home():
    return render_template("index.html", name="Sam")

@views.route("/sfx")
def sfx():
    return render_template("sfx.html")

@views.route("/gifs")
def gifs():
    return render_template("gifs.html")

@views.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        name = request.form["name"]
        return redirect(url_for("views.profile", name=name))
    else:
        return render_template("login.html")

@views.route("/profile")
def profile():
    name = request.args.get("name")
    return render_template("profile.html", name=name)

# @views.route("/json")
# def get_json():
#     return jsonify({"username": "Sam"})

# @views.route("/data")
# def get_data():
#     data = request.json
#     return jsonify(data)

# @views.route("/go-to-home")
# def go_to_home():
#     return redirect(url_for("views.home"))

# @views.route("/profile/<name>")
# def named_profile(name):
#     return render_template("profile.html", name=name)