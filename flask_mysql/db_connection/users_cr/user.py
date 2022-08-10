from flask.config.mysqlconnection import connectToMySQL

class user:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data ['first_name']
        self.last_name = data ['last_name']
        self.email = data ['email']