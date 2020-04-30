from flask_wtf import FlaskForm
from wtforms import StringField, validators

class ClubForm(FlaskForm):
    name = StringField("Club name", [validators.Length(min=3, max=20)])
    hobby = StringField("Hobby name", [validators.Length(min=3, max=20)])

    class Meta:
        csrf = False

class ChangeClubNameForm(FlaskForm):
    name = StringField("Club name", [validators.Length(min=3, max=20)])

    class Meta:
        csrf = False

class ChangeClubHobbyForm(FlaskForm):
    hobby = StringField("Club name", [validators.Length(min=3, max=20)])

    class Meta:
        csrf = False
