from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, SigninForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)

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

    print("POST - /auth/signin")
    form = SigninForm(request.form)
    print("form: ", form)
    user = User(form.name.data, form.username.data, form.password.data)

    db.session().add(user)
    db.session().commit()

    login_user(user)
    return redirect(url_for("index"))

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))
