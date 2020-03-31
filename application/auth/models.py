from application import db
from application.models import Base

from sqlalchemy.sql import text

GENDERS = ('Male', 'Female')

class User(Base):
    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))

    clubs = db.relationship("Club", backref='account', lazy=True)
    equipments = db.relationship("Equipment", backref='account', lazy=True)

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    @staticmethod
    def find_club_leaders():
        stmt = text("SELECT Account.id, Account.name, COUNT(Club.id)"
                " FROM Account, Club"
                " WHERE Club.leader_id = Account.id"
                " GROUP BY Account.id")
        res = db.engine.execute(stmt)

        response = [ {
            "id": row[0],
            "name": row[1],
            "clubs": row[2]
            } for row in res ]
        return response
