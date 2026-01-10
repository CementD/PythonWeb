from extensions import db

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    gamer_id = db.Column(db.Integer, db.ForeignKey('gamer.id'), unique=True)
    gamer = db.relationship('Gamer', back_populates='profile')
