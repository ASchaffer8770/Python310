from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

#CREATES THE AUTHOR CLASS
class Author: 
    def __init__ (self,data):
        self.id = data ['id']
        self.name = data ['name']
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']

#CLASSMETHODS WHICH ALLOW US TO create AUTHORs
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        result = connectToMySQL(DATABASE).query_db(query)
        all_authors = []
        for db_row in result:
            author_instance = cls(db_row)
            all_authors.append(author_instance)
        return all_authors

    @classmethod
    def create(cls,data): #create a new author
        query = "INSERT INTO authors (name) VALUES (%(name)s)"
        return connectToMySQL(DATABASE).query_db(query, data)

#GET ONE BY ID
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM authors WHERE id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        if result:
            author_instance = cls(result[0])
            return author_instance
        return result