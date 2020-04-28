from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application import app, db
from application.auth.models import User, GENDERS

from application.user.forms import ChangeNameForm, ChangeAgeForm, ChangeGenderForm

from application.equipments.forms import EquipmentForm

@app.route("/user", methods=["GET"])
def users_index():
    return render_template("user/list.html", users = User.query.all())

@app.route("/user/<user_id>/", methods=["GET"])
def user_page(user_id):
    user = User.query.get(user_id)
    if not user:
        return redirect(url_for("index"))

    return render_template("user/user.html",
            user = user,
            equipmentForm = EquipmentForm(),
            changeNameForm=ChangeNameForm(),
            changeAgeForm=ChangeAgeForm(),
            changeGenderForm=ChangeGenderForm()
            )

@app.route("/user/update/name/<user_id>/", methods=["POST"])
@login_required
def user_change_name(user_id):
    user = User.query.get(user_id)
    if not user:
        return redirect(url_for("index"))

    form = ChangeNameForm(request.form)
    if not form.validate():
        return render_template("user/user.html",
                user = user,
                equipmentForm=EquipmentForm(),
                changeNameForm=form,
                changeAgeForm=ChangeAgeForm(),
                changeGenderForm=ChangeGenderForm()
                )

    user.name = form.name.data
    db.session().commit()
    return redirect(url_for("user_page", user_id = user.id))

@app.route("/user/update/age/<user_id>/", methods=["POST"])
@login_required
def user_change_age(user_id):
    user = User.query.get(user_id)
    if not user:
        return redirect(url_for("index"))

    form = ChangeAgeForm(request.form)
    if not form.validate():
        return render_template("user/user.html",
                user = user,
                equipmentForm=EquipmentForm(),
                changeNameForm=ChangeNameForm(),
                changeAgeForm=form,
                changeGenderForm=ChangeGenderForm()
                )

    user.age = form.age.data
    db.session().commit()
    return redirect(url_for("user_page", user_id = user.id))

@app.route("/user/update/gender/<user_id>/", methods=["POST"])
@login_required
def user_change_gender(user_id):
    user = User.query.get(user_id)
    if not user:
        return redirect(url_for("index"))

    form = ChangeGenderForm(request.form)
    if not form.validate():
        return render_template("user/user.html",
                user = user,
                equipmentForm=EquipmentForm(),
                changeNameForm=ChangeNameForm(),
                changeAgeForm=ChangeAgeForm(),
                changeGenderForm=form
                )

    user.gender = form.gender.data
    db.session().commit()
    return redirect(url_for("user_page", user_id = user.id))

@app.route("/user/<user_id>/follow/<follow_id>/", methods=["POST"])
@login_required
def user_follow(user_id, follow_id):
    user = User.query.get(user_id)
    if not user:
        return redirect(url_for("index"))
    if user != current_user:
        return redirect(url_for("user_page", user_id = user.id))

    followed = User.query.get(follow_id)
    if not followed:
        return redirect(url_for("user_page", user_id = user.id))

    user.following.append(followed)
    db.session.commit()
    return redirect(url_for("user_page", user_id=followed.id))
