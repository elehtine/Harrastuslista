from flask import redirect, render_template, request, url_for
from flask_login import login_required, current_user

from application import app, db
from application.equipments.models import Equipment
from application.equipments.forms import EquipmentForm

@app.route("/equipments/", methods=["POST"])
@login_required
def equipment_add():
    form = EquipmentForm(request.form)
    if not form.validate():
        return redirect(url_for("user_page"))

    equipment = Equipment(form.equipment.data)
    equipment.account_id = current_user.id

    db.session().add(equipment)
    db.session().commit()

    return redirect(url_for('user_page', user_id=current_user.id))

@app.route("/equipments/<equipment_id>/delete", methods=["POST"])
@login_required
def equipment_delete(equipment_id):
    equipment = Equipment.query.get(equipment_id)

    if current_user.id != equipment.account_id:
        return redirect(url_for("user_page", user_id = equipment.account_id))

    db.session().delete(equipment)
    db.session().commit()

    return redirect(url_for("user_page", user_id = equipment.account_id))


