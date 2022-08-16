from flask import Flask, render_template, session, request, redirect
from dog_model import Dog #imports dog class from the dog model gives access to queries

app = Flask(__name__)

@app.route('/')
def index():
    all_dogs = Dog.get_all() #stores all dog query in the variable all_dogs
    return render_template("index.html", dogs = all_dogs)

if __name__=="__main__": 
    app.run(debug=True)