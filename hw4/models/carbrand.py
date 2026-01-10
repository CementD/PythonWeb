from extensions import db

class Carbrand(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)
    models = db.relationship('Carmodel', back_populates='brand', lazy=True)