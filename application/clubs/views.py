from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.clubs.models import Club
from application.clubs.forms import ClubForm
from application.messages.forms import MessageForm

@app.route("/clubs", methods=["GET"])
def clubs_index():
    return render_template("clubs/list.html", clubs = Club.query.all())

@app.route("/clubs/new/")
@login_required
def clubs_form():
    return render_template("clubs/new.html", form = ClubForm())

@app.route("/clubs/", methods=["POST"])
@login_required
def clubs_create():
    form = ClubForm(request.form)

    if not form.validate():
        return render_template("clubs/new.html", form = form)

    club = Club(form.name.data, form.hobby.data)
    club.leader_id = current_user.id

    db.session().add(club)
    db.session().commit()
  
    return redirect(url_for("clubs_index"))

@app.route("/clubs/delete/<club_id>", methods=["POST"])
@login_required
def clubs_delete(club_id):
    club = Club.query.get(club_id)

    if current_user.id != club.leader_id:
        return redirect(url_for("clubs_index"))


    db.session().delete(club)
    db.session().commit()
  
    return redirect(url_for("clubs_index"))

@app.route("/clubs/<club_id>", methods=["GET"])
def club_page(club_id):
    club = Club.query.get(club_id)
    return render_template("clubs/club.html", club=club, messageForm=MessageForm())

@app.route("/clubs/join/<club_id>", methods=["POST"])
@login_required
def club_join(club_id):
    club = Club.query.get(club_id)

    if current_user in club.members:
        return render_template("clubs/club.html", club=club)

    club.members.append(current_user)
    db.session().commit()
    return render_template("clubs/club.html", club=club, messageForm=MessageForm())
