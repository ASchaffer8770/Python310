from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninjas_model import Ninja

#read all route
@app.route('/home')
@app.route('/')
def dojo_home():
    all_dojos = Dojo.get_all()
    print(all_dojos)
    return render_template ('home.html', all_dojos = all_dojos)

#create dojo
@app.route('/new/dojo')
def new_dojo():
    return render_template ('new_dojo.html')

@app.route('/create/dojo')
def create_dojo():
    Dojo.create(request.form)
    return redirect('/')

#Read one dojo with all ninjas in it
@app.route('/dojo/<int:id>')
def dojo_show(id):
    data = {
        "id":id
    }
    dojo = Dojo.read_one(data)
    return render_template('dojo_ninjas.html', dojo = dojo)
