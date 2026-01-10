from extensions import db
from models.associations import gamer_game

class Gamer(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    games = db.relationship(
        'Game',
        secondary=gamer_game,
        back_populates='gamers'
    )

    profile = db.relationship('Profile', back_populates='gamer', uselist=False)
