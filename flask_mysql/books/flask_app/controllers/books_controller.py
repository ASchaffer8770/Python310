from flask_app import app 
from flask import render_template, redirect, session, request
from flask_app.models.books_model import Book

#READ ALL ROUTE
@app.route('/books')
def books_home():
    all_books = Book.get_all()
    return render_template('books.html', all_books = all_books)

#CREATE NEW BOOK
@app.route('/new/book')
def new_book():
    return render_template ('author.html')

@app.route('/create/book', methods=['POST'])
def create_book():
    Book.create(request.form)
    return redirect('/books')