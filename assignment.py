#Assignment: Lab M04
#Name: James Ramsey
#Creates CRUD API for books 

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)



app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
db = SQLAlchemy(app)

class book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_name = db.Column(db.String(80), unique=True,nullable=False)
    author = db.Column(db.String(120))
    publisher = db.Column(db.String(120))

    def __repr__(self):
        return f"{self.book_name} - {self.author}"

@app.route('/')
def index():
    return 'do I work'

@app.route('/books')
def get_books():
    books = book.query.all()
    
    output = []
    for book in books:
        book_data = {'book_name': book.book_name, 'author': book.descripiton, 'publisher': book.publisher}

        output.append(book_data)
    return {"books": output}

@app.route('/books/<id>')
def get_book(id):
    book = book.query.get_or_404(id)
    return {"book_name": book.book_name, "author": book.author, 'publisher': book.publisher}

#allows addition of books
@app.route('/books', methods = ['POST'])
def add_book():
    book = book(book_name=request.json['book_name'], author = request.json['author'])
    db.session.add(book)
    db.session.commit()
    return {'id': book.id}

#allows user to delete books
@app.route('/books/<id>', methods = ['DELETE'])
def delete_book(id):
    book = book.query.get(id)
    if book is None:\
        return {"error" : "not found"}
    db.session.delete(book)
    db.session.commit()
    return {"message": "Item deleted"}

# I'm not entirely sure if this works or not I followed the video and spent the entire weekend on it but I keep running into errors and 
# I ran into an error that I couldn't find a fix for sorry