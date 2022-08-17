from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.users_model import User

#READ ALL ROUTE (DISPLAYS ALL USERS IN DB)
@app.route('/')
@app.route('/users')
def index():
    all_users = User.get_all() #stores all users into the variable all_users
    return render_template('read.html', users = all_users)

#CREATE ROUTE
@app.route('/users/new') #render form input to create new user this displays the form
def new_user_form():
    return render_template('create.html')

@app.route('/users/create', methods=['POST']) #ACTION ROUTE TO CREATE USER IN DB
def new_user():
    User.create(request.form)
    return redirect('/users')

#READ ONE ROUTE
@app.route('/users/<int:id>')
@app.route('/users/show/<int:id>') #This route reads the id in the url and displays it its own page
def display_one(id):
    data = {
        "id":id
    }
    user = User.get_one(data)
    return render_template('read_one.html', user=user)

#UPDATE/EDIT ROUTE
@app.route('/users/<int:id>/edit') #display the edit form
def display_edit(id):
    data = {
        "id":id
    }
    user = User.get_one(data)
    return render_template('edit.html', user=user)

@app.route('/users/<int:id>/update', methods=['POST'])#action route that is not working
def update(id):
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "id":id
    }
    User.update(data)
    return redirect (f'/users/{id}')

#Delete route
@app.route("/users/<int:id>/delete")
def delete_user(id):
    data = {
        "id":id
    }
    User.delete(data)
    return redirect('/')