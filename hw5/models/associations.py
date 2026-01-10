from extensions import db

gamer_game = db.Table(
    'gamer_game',
    db.Column('gamer_id', db.Integer, db.ForeignKey('gamer.id')),
    db.Column('game_id', db.Integer, db.ForeignKey('game.id'))
)