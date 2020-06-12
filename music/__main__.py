import os
import shutil
import argparse
from music.server import app

parser = argparse.ArgumentParser()

parser.add_argument("--port", default=8000, type=int)
parser.add_argument("--debug", default=False, action="store_true")
parser.add_argument("--add-dummy-data", default=False, action="store_true")
args = parser.parse_args()

if args.add_dummy_data:
    from music.server import db, Music
    from music.test_data import data

    if not os.path.exists("music/static"):
        os.mkdir("music/static")
    for title, artists, album in data:
        m = Music.new_upload(
            title=title, artists=artists, album=album, content=title.encode()
        )
        db.session.add(m)
        target = f"music/static/{m.md5}.mp3"
        if not os.path.exists(target):
            shutil.copyfile(os.path.abspath("music/static/kammo"), target)
    db.session.commit()

app.run(port=args.port, debug=args.debug)
