from flask import Flask
app = Flask(__name__)
app.secret_key = "this is not a secret"

DATABASE = "login"