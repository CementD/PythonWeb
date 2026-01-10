from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return (f'Book {self.title} by {self.author}')

with app.app_context():
    db.create_all()


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route("/books")
def books():
    books = Book.query.all()
    return render_template("books.html", books=books)

@app.route("/books/add")
def add():
    return render_template("add_book.html")

@app.route("/books/add", methods=["POST"])
def add_book():
    title = request.form['title']
    author = request.form['author']
    year = request.form['year']
    book = Book(title=title, author=author, year=year)
    db.session.add(book)
    db.session.commit()
    return redirect("/books")

@app.route('/books/<int:id>/edit')
def edit(id):
    book = Book.query.get_or_404(id)
    return render_template('edit_book.html', book=book)

@app.route('/books/<int:id>/update', methods = ['POST'])
def update(id):
    book = Book.query.get_or_404(id)
    book.title = request.form['title']
    book.author = request.form['author']
    book.year = request.form['year']
    db.session.commit()
    return redirect('/books')

@app.route('/books/<int:id>/delete', methods = ['POST'])
def delete(id):
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()
    return redirect('/books')

if __name__ == '__main__':
    app.run()
