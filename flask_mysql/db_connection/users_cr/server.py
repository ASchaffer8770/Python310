from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/submit', methods = ['POST'])
def submit():

    return redirect ('/create')

if __name__ == "__main__":
    app.run(debug=True)