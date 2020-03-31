from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.equipments.models import Equipment
from application.equipments.forms import EquipmentForm
from application.auth.forms import OptionsForm

@app.route("/equipments/", methods=["POST"])
@login_required
def equipment_add():
    form = EquipmentForm(request.form)
    if not form.validate():
        return render_template("auth/user.html",
                user = current_user,
                equipmentForm = form,
                optionsForm = OptionsForm()
                )

    equipment = Equipment(form.equipment.data)
    equipment.account_id = current_user.id

    db.session().add(equipment)
    db.session().commit()

    return redirect(url_for('user_page', user_id=current_user.id))
