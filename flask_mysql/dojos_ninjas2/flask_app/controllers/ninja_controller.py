from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.ninjas_model import Ninja

#read all route
@app.route('/')
def home():
    return render_template ('home.html')
