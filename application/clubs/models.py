from application import db
from application.models import Base

from sqlalchemy.sql import text

from application.auth.models import User

member_table = db.Table('members',
        db.Column('club_id', db.Integer, db.ForeignKey('club.id'), primary_key=True),
        db.Column('account_id', db.Integer, db.ForeignKey('account.id'), primary_key=True)
        )

class Club(Base):
    name = db.Column(db.String(144), nullable=False)
    hobby = db.Column(db.String(144), nullable=False)

    leader_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    members = db.relationship('User', secondary=member_table,
            backref=db.backref('joined', lazy='dynamic'))

    messages = db.relationship("Message", backref='account', lazy='dynamic')

    def __init__(self, name, hobby):
        self.name = name
        self.hobby = hobby

    def get_leader(self):
        return User.query.get(self.leader_id)
