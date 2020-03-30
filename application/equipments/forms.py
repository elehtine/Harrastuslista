from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField

class EquipmentForm(FlaskForm):
    name = StringField("Equipment")

    class Meta:
        csrf = False
