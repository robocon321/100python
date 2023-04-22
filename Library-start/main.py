# import sqlite3
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# db = sqlite3.connect("books-collection.db")
# cursor = db.cursor()
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")
# cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
# db.commit()

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///new-books-collection.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, db.Sequence('seq_reg_id', start=1, increment=1), primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float(120), nullable=False)

    def __repr__(self):
        return f'<Book {self.title}>'

db.create_all()

# book1 = Book(id = 1, title = "Book 1", author = "Author 1", rating = 9.8)
# book2 = Book(id = 2, title = "Book 2", author = "Author 2", rating = 7.7)
# book3 = Book(id = 3, title = "Book 3", author = "Author 3", rating = 8.2)
#
# db.session.add(book1)
# db.session.add(book2)
# db.session.add(book3)
#
# db.session.commit()


@app.route('/')
def home():
    all_books = Book.query.all()
    return render_template('index.html', books = all_books)


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == 'POST':
        book = Book(title=request.form['title'], author=request.form['author'], rating=request.form['rating'])
        db.session.add(book)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add.html')

@app.route("/delete/<book_id>")
def delete(book_id):
    book = Book.query.get(book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect('/')

@app.route("/update/<book_id>")
def detail(book_id):
    book = Book.query.get(book_id)
    return render_template('update.html', book=book)

@app.route("/update", methods=["POST"])
def update():
    book = Book.query.get(request.form['id'])
    book.rating = request.form['rating']
    db.session.commit()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

