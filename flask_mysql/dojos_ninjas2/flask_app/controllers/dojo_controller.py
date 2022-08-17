from flask_app import app
from flask import render_template, redirect, session, request
from flask_app.models.dojo_model import Dojo

#read all route
@app.route('/')
def dojo_home():
    return render_template ('home.html')