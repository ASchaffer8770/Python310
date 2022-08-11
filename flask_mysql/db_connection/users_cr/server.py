from flask import Flask, render_template, redirect, request, session

from user import users

app = Flask(__name__)

@app.route('/')
def index():
    return redirect ('/users')

@app.route('/users')
def users():
    return render_template("read.html", users = users.get_all())

if __name__ == "__main__":
    app.run(debug=True)