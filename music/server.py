import hashlib
from sqlalchemy import Column, Integer, String, or_
from sqlalchemy.orm import relationship

from flask import Flask, url_for, redirect, render_template, request, abort
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
db = SQLAlchemy(app)


class Music(db.Model):
    md5 = db.Column(db.String, primary_key=True)
    title = db.Column(db.String)
    artists = db.Column(db.String)
    album = db.Column(db.String)

    @property
    def play_url(self):
        return url_for("play", slug=self.md5)

    @staticmethod
    def new_upload(*, content, **kwargs):
        return Music(md5=hashlib.md5(content).hexdigest(), **kwargs)

    def display(self, query=None):
        if query is not None:
            if query in self.title:
                return self.title
            if query in self.artists:
                return f"{self.title}: {self.artists}"
            if query in self.album:
                return f"{self.title}: {self.album}"
        return f"{self.title}: {self.album} : {self.artists}"


db.create_all()


@app.route("/<offset>-<limit>", methods=["GET", "POST"])
@app.route("/", methods=["GET", "POST"])
def home(offset=0, limit=1000):
    # Pagination needs to be added. This large limit should suffice till then
    matches = []
    if request.method == "POST" and "query" in request.form:
        query = request.form.get("query")
        matches = (
            db.session.query(Music)
            .filter(
                or_(
                    Music.title.contains(query),
                    Music.artists.contains(query),
                    Music.album.contains(query),
                )
            )
            .limit(5)
        )
    return render_template(
        "home.html",
        matches=matches,
        query=query if query is not None else "",
        music_titles=db.session.query(Music)
        .order_by(Music.title)
        .offset(offset)
        .limit(limit),
    )


@app.route("/m", methods=["POST"])
def upload_a_file():
    pass


@app.route("/m/<slug>", methods=["GET"])
def play(slug):
    m = db.session.query(Music).filter_by(md5=slug).first()
    if m is None:
        abort(404)
    return render_template(
        "player.html",
        slug=m.md5,
        title=m.title,
        artists=m.artists if m.artists else "Unknown artists",
        album=m.album if m.album else "Unknown album",
    )


@app.route("/m/<slug>", methods=["DELETE"])
def delete_a_file(slug):
    pass
