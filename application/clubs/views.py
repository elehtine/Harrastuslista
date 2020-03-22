from flask import redirect, render_template, request, url_for

from application import app, db
from application.clubs.models import Club
from application.clubs.forms import ClubForm

@app.route("/clubs", methods=["GET"])
def clubs_index():
    return render_template("clubs/list.html", clubs = Club.query.all())

@app.route("/clubs/new/")
def clubs_form():
    return render_template("clubs/new.html", form = ClubForm())

@app.route("/clubs/<club_id>/", methods=["POST"])
def clubs_set_name(club_id):
    club = Club.query.get(club_id)
    club.name = request.form.get("name")

    db.session().commit()

    return redirect(url_for("clubs_index"))

@app.route("/clubs/", methods=["POST"])
def clubs_create():
    form = ClubForm(request.form)

    if not form.validate():
        return render_template("clubs/new.html", form = form)

    club = Club(form.name.data, form.hobby.data)

    db.session().add(club)
    db.session().commit()
  
    return redirect(url_for("clubs_index"))
