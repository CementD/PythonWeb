from extensions import db

class Carmodel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey('carbrand.id'), nullable=False)
    brand = db.relation('Carbrand', back_populates='models')