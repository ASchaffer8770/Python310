from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

class Dojo: #creates the dojo class
    def __init__ (self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


#add dojo methods below
    @classmethod
    def get_all(cls): #get all method for dojos
        query = "SELECT * FROM dojos;"
        result = connectToMySQL(DATABASE).query_db(query)
        print(result)
        all_dojos = []
        for row_from_db in result:
            dojo_instance = cls(row_from_db)
            all_dojos.append(dojo_instance)
        return all_dojos

    @classmethod
    def create(cls,data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def read_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if result:
            dojo_instance = cls(result[0])
            return dojo_instance
        return result