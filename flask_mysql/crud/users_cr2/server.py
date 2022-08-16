from flask import Flask, render_template, session, request, redirect
from users_model import User #HAVE TO IMPORT USER FROM THE MODEL TO DO DB QUERIES
app = Flask(__name__)


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
    return redirect('/')

if __name__=="__main__": 
    app.run(debug=True)