from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.clubs.models import Club
from application.clubs.forms import ClubForm, ChangeClubNameForm, ChangeClubHobbyForm
from application.messages.forms import MessageForm

from application.auth.models import User

@app.route("/clubs", methods=["GET"])
def clubs_index():
    return render_template("clubs/list.html", clubs = Club.query.all())

@app.route("/clubs/new")
@login_required
def clubs_form():
    return render_template("clubs/new.html", form = ClubForm())

@app.route("/clubs", methods=["POST"])
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

@app.route("/clubs/<club_id>/delete", methods=["POST"])
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
    return render_template("clubs/club.html", club=club,
            messageForm=MessageForm(),
            clubNameForm=ChangeClubNameForm(),
            clubHobbyForm=ChangeClubHobbyForm()
            )

@app.route("/clubs/<club_id>/join", methods=["POST"])
@login_required
def club_join(club_id):
    club = Club.query.get(club_id)

    if current_user in club.members:
        return render_template("clubs/club.html", club=club,
                messageForm=MessageForm(),
                clubNameForm=ChangeClubNameForm(),
                clubHobbyForm=ChangeClubHobbyForm()
                )

    club.members.append(current_user)
    db.session().commit()
    return render_template("clubs/club.html", club=club,
            messageForm=MessageForm(),
            clubNameForm=ChangeClubNameForm(),
            clubHobbyForm=ChangeClubHobbyForm()
            )

@app.route("/clubs/<club_id>/exit", methods=["POST"])
@login_required
def club_exit(club_id):
    club = Club.query.get(club_id)

    if current_user not in club.members:
        return render_template("clubs/club.html", club=club,
                messageForm=MessageForm(),
                clubNameForm=ChangeClubNameForm(),
                clubHobbyForm=ChangeClubHobbyForm()
                )

    club.members.remove(current_user)
    db.session().commit()
    return render_template("clubs/club.html", club=club,
            messageForm=MessageForm(),
            clubNameForm=ChangeClubNameForm(),
            clubHobbyForm=ChangeClubHobbyForm()
            )

@app.route("/clubs/<club_id>/kick/<user_id>", methods=["POST"])
@login_required
def club_kick(club_id, user_id):
    club = Club.query.get(club_id)
    user = User.query.get(user_id)
    if user not in club.members:
        return render_template("clubs/club.html", club=club,
                messageForm=MessageForm(),
                clubNameForm=ChangeClubNameForm(),
                clubHobbyForm=ChangeClubHobbyForm()
                )

    club.members.remove(user)
    db.session().commit()
    return redirect(url_for("club_page", club_id=club.id))

@app.route("/clubs/<club_id>/update/name", methods=["POST"])
@login_required
def change_club_name(club_id):
    club = Club.query.get(club_id)

    form = ChangeClubNameForm(request.form)
    if not form.validate():
        return render_template("clubs/club.html", club=club,
                messageForm=MessageForm(),
                clubNameForm=form,
                clubHobbyForm=ChangeClubHobbyForm()
                )

    club.name = form.name.data
    db.session().commit()
    return render_template("clubs/club.html", club=club,
            messageForm=MessageForm(),
            clubNameForm=ChangeClubNameForm(),
            clubHobbyForm=ChangeClubHobbyForm()
            )

@app.route("/clubs/<club_id>/update/hobby", methods=["POST"])
@login_required
def change_club_hobby(club_id):
    club = Club.query.get(club_id)

    form = ChangeClubHobbyForm(request.form)
    if not form.validate():
        return render_template("clubs/club.html", club=club,
                messageForm=MessageForm(),
                clubNameForm=ChangeClubNameForm,
                clubHobbyForm=form
                )

    club.hobby = form.hobby.data
    db.session().commit()
    return render_template("clubs/club.html", club=club,
            messageForm=MessageForm(),
            clubNameForm=ChangeClubNameForm(),
            clubHobbyForm=ChangeClubHobbyForm()
            )
