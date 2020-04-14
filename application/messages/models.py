from application import db
from application.models import Base

class Message(Base):
    message = db.Column(db.String(144), nullable=False)

    club_id = db.Column(db.Integer, db.ForeignKey('club.id'), nullable=False)

    def __init__(self, message):
        self.message = message
