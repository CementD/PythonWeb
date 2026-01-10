from extensions import db

class GameDeveloper(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    country = db.Column(db.String(50), nullable=False)

    games = db.relationship('Game', back_populates='developer')
