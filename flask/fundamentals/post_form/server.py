from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "THIS IS A SECRET KEY USED TO SETUP SESSION"

@app.route('/')
def index():
    return render_template ("index.html")

@app.route('/submit', methods = ['POST']) #accepts post from incoming form ACTION ROUTE
def submit():
    print(request.form)
    session['name'] = request.form['name'] #SESSION STORES THIS IN THE VARIABLE NAME
    session['age'] = request.form['age']
    if request.form['secret'] != "this_is_a_secret_value":
        return "Dont mess with the hidden value"
    session['secret'] = request.form['secret']

    return redirect ('/display') #DO NOT RENDER ON ACTION ROUTES INSTEAD REDIRECT

@app.route('/display') #THIS IS WHAT DISPLAYS THE INFO FROM SESSION
def display():
    return render_template('display.html')

if __name__=="__main__": 
    app.run(debug=True)