from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
import re
EMAIL_REGEX = re.compile(r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$")

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.update_at = data['update_at']
        
    @classmethod
    def create(cls,data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def user_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])


    @staticmethod
    def validate(user_data):
        is_valid = True
        if len(user_data['first_name']) < 2:
            flash('First name must be at least 2 characters', 'reg')
            is_valid = False
        if len(user_data['last_name']) < 2:
            flash('Last name must be at least 2 characters', 'reg')
            is_valid = False
        if len(user_data['email']) < 2:
            flash('Email must be at least 2 characters', 'reg')
            is_valid = False
        elif not EMAIL_REGEX.match(user_data['email']):
            is_valid = False
            flash('Invalid Email', 'reg')
        else:
            data = {
                'email': user_data['email']
            }
            potential_user = User.user_by_email(data)
            if potential_user:
                is_valid =  False
                flash("Email already in use")
        if len(user_data['password']) < 8:
            flash('Password must be more than 8 characters', 'reg')
            is_valid = False
        elif not user_data['password'] == user_data['confirm_pass']:
            flash("Passwords do not match")
            is_valid = False
        return is_valid