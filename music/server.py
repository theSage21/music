from flask import Flask, url_for, redirect, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/m", methods=["POST"])
def upload_a_file():
    pass


@app.route("/m/list", methods=["POST"])
def music_list():
    pass


@app.route("/m/search", methods=["POST"])
def music_search():
    pass


@app.route("/m/<slug>", methods=["GET"])
def get_a_file(slug):
    return render_template("player.html", slug=slug)


@app.route("/m/<slug>", methods=["DELETE"])
def delete_a_file(slug):
    pass
