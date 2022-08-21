from flask_app import app
from flask import render_template, redirect, session, request, flash
from flask_bcrypt import Bcrypt
from flask_app.models.users_model import User

bcrypt = Bcrypt(app)

# bcrypt.generate_password_hash(password_string)
# bcrypt.check_password_hash(hashed_password, password_string)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/welcome')
def welcome():
    if not "user_id" in session:
        return redirect('/')
    return render_template ('welcome.html')

@app.route("/users/register", methods =['POST']) # ACTION ROUTE
def register():
    if not User.validate(request.form):
        return redirect('/')
    hashed_pw = bcrypt.generate_password_hash(request.form['password'])
    data = {
        **request.form,
        'password' : hashed_pw
    }
    User.create(data)
    session['user_id'] = User.create(data)
    return redirect('/welcome')

@app.route("/users/logout")
def logout():
    del session['user_id']
    return redirect('/')

@app.route('/users/login', methods=['POST'])
def login():
    data = {
        'email': request.form['email']
    }
    user_from_db = User.user_by_email(data)
    if not user_from_db:
        flash("Invalid Credentials", "log")
        return redirect("/")
    if not bcrypt.check_password_hash(user_from_db.password, request.form['password']):
        