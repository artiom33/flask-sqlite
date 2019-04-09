from flask import render_template
from app import app, db


@app.route('/', defaults={'entries': 5})
@app.route('/<int:entries>')
def index(entries):
    db_query = "select * from iris limit %d" % entries
    res = db.engine.execute(db_query)
    return render_template("index.html", users=res.fetchall())
