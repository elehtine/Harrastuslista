from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

nameValidators = [validators.Length(min=3, max=70)]
usernameValidators = [validators.Length(min=2, max=20)]
passwordValidators = [validators.Length(min=4, max=20)]

class LoginForm(FlaskForm):
    username = StringField("Username", usernameValidators)
    password = PasswordField("Password", passwordValidators)

    class Meta:
        csrf = False

class SigninForm(FlaskForm):
    name = StringField("Name", nameValidators)
    username = StringField("Username", usernameValidators)
    password = PasswordField("Password", passwordValidators)

    class Meta:
        csrf = False
