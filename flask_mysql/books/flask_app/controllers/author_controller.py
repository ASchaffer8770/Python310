from flask_app import app 
from flask import render_template, redirect, session, request
from flask_app.models.author_model import Author

#READ ALL ROUTE
@app.route('/')
def author_home():
    all_authors = Author.get_all()
    return render_template('author.html', all_authors = all_authors)

#CREATE NEW AUTHOR
@app.route('/new/author')
def new_author():
    return render_template ('author.html')

@app.route('/create/author', methods=['POST'])
def create_author():
    Author.create(request.form)
    return redirect('/')