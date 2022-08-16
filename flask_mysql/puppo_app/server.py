from flask import Flask, render_template, session, request, redirect
from dog_model import Dog #imports dog class from the dog model gives access to queries

app = Flask(__name__)

#READ ALL ROUTE
@app.route('/')
def index():
    all_dogs = Dog.get_all() #stores all dog query in the variable all_dogs
    return render_template("index.html", dogs = all_dogs)

#READ ONE
@app.route('/dogs/<int:id>')
def display_one(id):
    data = {
        "id": id
    }
    dog = Dog.get_one(data)
    return render_template("one_dog.html", dog=dog)

#CREATE A DOG
@app.route('/dogs/new') #display route to render the form
def new_dog_form():
    return render_template("new_dog.html")

@app.route('/dogs/create', methods=['POST']) #Action route to actually create the dog in the db
def create_dog():
    Dog.create(request.form)
    return redirect('/')

if __name__=="__main__": 
    app.run(debug=True)