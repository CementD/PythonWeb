from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/planets')
def planets():
    planets_list = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
    moons = [0, 0, 1, 2, 97, 274, 29, 16]
    planets = []
    for planet in range(len(planets_list)):
        planets.append({
            "name": planets_list[planet],
            "moons": moons[planet]
        })
    return render_template('planets.html', planets=planets)

@app.route('/quotes')
def quotes():
    names = ["Sokrat", "Plato", "Aristotle", "Kant", "Niezsche"]
    quotes = ["The only true wisdom is in knowing you know nothing",
              "The measure of a man is what he does with power",
              "Knowing yourself is the beginning of all wisdom",
              "By a lie, a man throws away and, as it were, annihilates his dignity as a man",
              "God is dead"]

    quotes_dict = []
    for i in range(len(names)):
        quotes_dict.append({
            "name": names[i],
            "quote_item": quotes[i]
        })
    return render_template("quotes.html", quotes = quotes_dict)

@app.route('/favorite_celestial')
def favorite_celestial():
    return render_template('celestial_form.html')

@app.route('/submit1', methods=['POST'])
def submit1():
    celestail = request.form['celestail']
    if celestail == "":
        return "Please enter a celestial body"
    return f'Your celestial body is {celestail}'

@app.route('/discoveries')
def discoveries():
    discovers = ["America", "Saturn", "Neptune", "Pluto"]
    years = [1492, 1610, 1846, 1930]
    discoveries = []
    for i in range(len(discovers)):
        discoveries.append({
            "discover": discovers[i],
            "year": years[i]
        })
    return render_template("discoveries.html", discoveries=discoveries)

@app.route('/philosophy_quiz')
def philosophy_quiz():
    schools = ["Stoicism", "Epicureanism", "Skepticism"]
    return render_template('philosophy_quiz.html', schools=schools)

@app.route('/submit2', methods=['POST'])
def submit2():
    school = request.form['school']
    if school == "":
        return "Please choose a school"
    return f'You chose {school}. Learn more about its main ideas!'

if __name__ == '__main__':
    app.run()
