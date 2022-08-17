from sqlite3 import connect
from unittest import result
from mysqlconnection import connectToMySQL
DATABASE = "users_schema"

class User: #create the class of user by calling all attributes from the user table in db
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data ['updated_at']
    #this creates the ability to instanciate a User when we call on it later

#READ ALL METHOD
    @classmethod #this is where we put queries to pull and push data to db
    def get_all(cls):
        query = "SELECT * FROM users;"
        result = connectToMySQL(DATABASE).query_db(query)#QUERY_DB IS built into mysqlconnection
        # print(result)
        all_users = [] #this list and loop pushes all data from the request to the data for the cls for display
        for row_from_db in result:
            user_instance = cls(row_from_db)
            all_users.append(user_instance)
        return all_users

#READ ONE METHOD
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if result:
            user_instance = cls(result[0])
            return user_instance
        return result

#CREATE METHOD FOR USER
    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        return connectToMySQL(DATABASE).query_db(query, data)


#UPDATE AN USER ******************ROUTE OR METHOD DOES NOT WORK***************
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s,  last_name = %(last_name)s, email = %(emails)s WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

#DELETE USER
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s"
        return connectToMySQL(DATABASE).query_db(query, data)
        