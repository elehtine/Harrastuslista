from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User, GENDERS
from application.auth.forms import LoginForm, SigninForm, OptionsForm

from application.equipments.forms import EquipmentForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

    if not form.validate():
        return render_template("auth/loginform.html", form = form)

    user = User.query.filter_by(username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                error = "No such username or password")

    login_user(user)
    return redirect(url_for("index"))    

@app.route("/auth/signin", methods = ["GET", "POST"])
def auth_signin():
    if request.method == "GET":
        return render_template("auth/signinform.html", form = SigninForm())

    form = SigninForm(request.form)
    if not form.validate():
        return render_template("auth/signinform.html", form = form)

    user = User(form.name.data, form.username.data, form.password.data)

    db.session().add(user)
    db.session().commit()

    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))

@app.route("/user", methods=["GET"])
def users_index():
    return render_template("auth/list.html", users = User.query.all())


@app.route("/user/<user_id>/", methods=["GET"])
def user_page(user_id):
    user = User.query.get(user_id)
    if not user:
        return redirect(url_for("index"))

    return render_template("auth/user.html",
            user = user,
            equipmentForm = EquipmentForm(),
            optionsForm = OptionsForm()
            )

@app.route("/user/<user_id>/", methods=["POST"])
def user_options(user_id):
    user = User.query.get(user_id)
    if not user:
        return redirect(url_for("index"))

    form = OptionsForm(request.form)

    if not form.validate():
        return render_template("auth/user.html",
                user = user,
                equipmentForm = EquipmentForm(),
                optionsForm = form
                )

    user.name = form.name.data
    user.age = form.age.data
    user.gender = form.gender.data

    db.session().commit()

    return redirect(url_for("user_page", user_id = user.id))
