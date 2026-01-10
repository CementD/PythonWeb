from flask import Flask
from extensions import db, migrate
from models import Game, GameDeveloper, Profile, Gamer

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate.init_app(app, db)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/fill_db')
def fill_db():
    valve = GameDeveloper.query.filter_by(name="Valve").first()
    if not valve:
        valve = GameDeveloper(
            name="Valve",
            year=1996,
            country="USA"
        )
        db.session.add(valve)

    rockstar = GameDeveloper.query.filter_by(name="Rockstar Games").first()
    if not rockstar:
        rockstar = GameDeveloper(
            name="Rockstar Games",
            year=1998,
            country="USA"
        )
        db.session.add(rockstar)

    hl = Game.query.filter_by(name="Half-Life").first()
    if not hl:
        hl = Game(
            name="Half-Life",
            year=1998,
            genre="FPS",
            developer=valve
        )
        db.session.add(hl)

    portal = Game.query.filter_by(name="Portal").first()
    if not portal:
        portal = Game(
            name="Portal",
            year=2007,
            genre="Puzzle",
            developer=valve
        )
        db.session.add(portal)

    gta = Game.query.filter_by(name="GTA V").first()
    if not gta:
        gta = Game(
            name="GTA V",
            year=2013,
            genre="Action",
            developer=rockstar
        )
        db.session.add(gta)

    gamer1 = Gamer.query.first()
    if not gamer1:
        gamer1 = Gamer()
        db.session.add(gamer1)

    gamer2 = Gamer.query.offset(1).first()
    if not gamer2:
        gamer2 = Gamer()
        db.session.add(gamer2)

    if not gamer1.profile:
        profile1 = Profile(
            username="gamer1",
            country="USA",
            gamer=gamer1
        )
        db.session.add(profile1)

    if not gamer2.profile:
        profile2 = Profile(
            username="gamer2",
            country="Germany",
            gamer=gamer2
        )
        db.session.add(profile2)

    if hl not in gamer1.games:
        gamer1.games.append(hl)

    if portal not in gamer1.games:
        gamer1.games.append(portal)

    if portal not in gamer2.games:
        gamer2.games.append(portal)

    if gta not in gamer2.games:
        gamer2.games.append(gta)

    db.session.commit()
    return "Database filled successfully!"

@app.route('/read_db')
def read_db():
    output = ""

    developers = GameDeveloper.query.all()
    output += "<h2>Developers</h2>"
    for developer in developers:
        output += (
            f"<p><b>ID:</b> {developer.id}, "
            f"<b>Name:</b> {developer.name}, "
            f"<b>Year:</b> {developer.year}, "
            f"<b>Country:</b> {developer.country}</p>"
        )
        if developer.games:
            output += f"<h4>Games ({len(developer.games)})</h4>"
            output += "<ul>"
            for game in developer.games:
                output += (
                    f"<li><b>ID:</b> {game.id}, "
                    f"<b>Name:</b> {game.name}, "
                    f"<b>Year:</b> {game.year}, "
                    f"<b>Genre:</b> {game.genre}</li>"
                )
                if game.gamers:
                    output += f"<p>Gamers ({len(game.gamers)})</p>"
                    output += "<ul>"
                    for gamer in game.gamers:
                        output += (
                            f"<li><b>ID:</b> {gamer.id}, "
                            f"<b>Username:</b> {gamer.profile.username}, "
                            f"<b>Country:</b> {gamer.profile.country}</li>"
                        )
                    output += "</ul>"
            output += "</ul>"
    return output


if __name__ == '__main__':
    app.run()
