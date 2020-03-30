from application import db
from application.models import Base

from application.auth.models import User

class Club(Base):
    name = db.Column(db.String(144), nullable=False)
    hobby = db.Column(db.String(144), nullable=False)

    leader_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    def __init__(self, name, hobby):
        self.name = name
        self.hobby = hobby

    def get_leader(self):
        return User.query.get(self.leader_id)
