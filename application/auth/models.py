from application import db
from application.models import Base

from sqlalchemy.sql import text

GENDERS = ('Male', 'Female')

follower_table = db.Table('follower_table',
        db.Column('followed_id', db.Integer, db.ForeignKey('account.id'), primary_key=True),
        db.Column('follower_id', db.Integer, db.ForeignKey('account.id'), primary_key=True)
        )

class User(Base):
    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)

    age = db.Column(db.Integer)
    gender = db.Column(db.String(10))

    clubs = db.relationship("Club", backref='account', lazy=True)
    equipments = db.relationship("Equipment", backref='account', lazy=True)

    following = db.relationship('User', secondary=follower_table,
            primaryjoin=("follower_table.c.follower_id == User.id"),
            secondaryjoin=("follower_table.c.followed_id == User.id"),
            backref=db.backref('followers', lazy='dynamic'), lazy='dynamic')

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
