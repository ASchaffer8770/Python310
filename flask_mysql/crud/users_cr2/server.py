from flask_app import app
from flask_app.controllers import users_controller #as you add more controllers for models import them here

if __name__=="__main__": 
    app.run(debug=True)