from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.messages.models import Message
from application.messages.forms import MessageForm
from application.clubs.models import Club

@app.route("/messages/<club_id>", methods=["POST"])
@login_required
def message_add(club_id):
    club = Club.query.get(club_id)
    if not club or current_user.id != club.leader_id:
        return redirect(url_for("clubs_index"))

    form = MessageForm(request.form)
    if not form.validate():
        return render_template("clubs/club.html", club=club)

    message = Message(form.message.data)
    message.club_id = club.id

    db.session().add(message)
    db.session().commit()

    return redirect(url_for("club_page", club_id=club.id))

@app.route("/messages/<club_id>/delete/<message_id>", methods=["POST"])
@login_required
def message_delete(club_id, message_id):
    club = Club.query.get(club_id)
    if not club or current_user.id != club.leader_id:
        return redirect(url_for("clubs_index"))

    message = Message.query.get(message_id)
    if not message:
        return render_template("clubs/club.html", club=club)

    db.session().delete(message)
    db.session().commit()

    return redirect(url_for("club_page", club_id=club.id))
