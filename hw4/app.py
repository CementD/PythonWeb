from flask import Flask
from extensions import db, migrate
from models import Carbrand, Carmodel

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
    data = {
        "Suzuki": ("Japan", [("Swift", 2022), ("Vitara", 2021), ("Jimny", 2023), ("Baleno", 2020)]),
        "BMW": ("Germany", [("3 Series", 2022), ("5 Series", 2021), ("X5", 2023), ("Z4", 2020)]),
        "Volkswagen": ("Germany", [("Golf", 2022), ("Passat", 2021), ("Tiguan", 2023), ("Polo", 2020)]),
        "Toyota": ("Japan", [("Corolla", 2022), ("Camry", 2021), ("RAV4", 2023), ("Prius", 2020)]),
        "Mitsubishi": ("Japan", [("Lancer", 2018), ("Outlander", 2021), ("Pajero", 2019), ("Eclipse", 2017)]),
        "Ford": ("USA", [("Fiesta", 2019), ("Focus", 2020), ("Mustang", 2022), ("Explorer", 2021)])
    }

    for brand_name, (country, models_list) in data.items():
        brand = Carbrand.query.filter_by(name=brand_name).first()
        if not brand:
            brand_obj = Carbrand(name=brand_name, country=country)
            db.session.add(brand_obj)
            db.session.flush()

        for model_name, year in models_list:
            model_obj = Carmodel.query.filter_by(name=model_name, brand_id=brand.id).first()
            if not model_obj:
                model_obj = Carmodel(name=model_name, year=year, brand=brand)
                db.session.add(model_obj)

    db.session.commit()
    return "Database was filled successfully!"

@app.route('/read_db')
def read_db():
    output = ""
    brands = Carbrand.query.all()
    output += "<h2>Brands</h2>"
    for brand in brands:
        output += f"<p>ID: {brand.id}, Name: {brand.name}, Country: {brand.country}</p>"

        if brand.models:
            output += "<ul>"
            for model in brand.models:
                output += f"<li>Model: {model.name}, Year: {model.year}</li>"
            output += "</ul>"
    return output


if __name__ == '__main__':
    app.run()
