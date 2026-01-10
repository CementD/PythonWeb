from extensions import db
from models.associations import gamer_game

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    genre =db.Column(db.String(50), nullable=False)

    developer_id = db.Column(db.Integer, db.ForeignKey('game_developer.id'), nullable=False)
    developer = db.relationship('GameDeveloper', back_populates='games')

    gamers = db.relationship(
        'Gamer',
        secondary=gamer_game,
        back_populates='games'
    )