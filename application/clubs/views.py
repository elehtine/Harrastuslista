from application import app, db
from flask import redirect, render_template, request, url_for
from application.clubs.models import Club

@app.route("/clubs", methods=["GET"])
def clubs_index():
    return render_template("clubs/list.html", clubs = Club.query.all())

@app.route("/clubs/new/")
def clubs_form():
    return render_template("clubs/new.html")

@app.route("/clubs/<club_id>/", methods=["POST"])
def clubs_set_name(club_id):
    club = Club.query.get(club_id)
    club.name = request.form.get("name")

    db.session().commit()

    return redirect(url_for("clubs_index"))

@app.route("/clubs/", methods=["POST"])
def clubs_create():
    f = request.form
    club = Club(f.get("name"), f.get("hobby"))

    db.session().add(club)
    db.session().commit()
  
    return redirect(url_for("clubs_index"))
