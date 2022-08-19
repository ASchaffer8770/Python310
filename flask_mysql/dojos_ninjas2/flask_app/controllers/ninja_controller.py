from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninjas_model import Ninja

#create route for ninja
@app.route('/ninja/new')
def new_ninja():
    all_dojos = Dojo.get_all()#this calls dojos to populate list
    return render_template('new_ninja.html', all_dojos = all_dojos)

@app.route('/ninja/create', methods = ['POST'])
def create_ninja():
    Ninja.create(request.form)
    return redirect(f"/dojo/{request.form['dojo_id']}")# this pulls the dojo id and routes us to the read one