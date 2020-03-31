from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, validators

class EquipmentForm(FlaskForm):
    name = StringField("Equipment", [validators.Length(min=2, max=35)])

    class Meta:
        csrf = False
