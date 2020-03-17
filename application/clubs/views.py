from application import app, db
from flask import render_template, request
from application.clubs.models import Club

@app.route("/clubs/", methods=["GET"])
def clubs_index():
    return render_template("clubs/list.html", clubs = Club.query.all())

@app.route("/clubs/new/")
def clubs_form():
    print("/clubs/new/")
    return render_template("clubs/new.html")

@app.route("/clubs/", methods=["POST"])
def clubs_create():
    f = request.form
    club = Club(f.get("name"), f.get("hobby"))

    db.session().add(club)
    db.session().commit()
  
    return redirect(url_for("tasks_index"))
