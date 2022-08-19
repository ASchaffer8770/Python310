from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE

#CREATES THE BOOKS CLASS
class Book: 
    def __init__ (self,data):
        self.id = data ['id']
        self.title = data ['title']
        self.num_of_pages = data ['num_of_pages']
        self.created_at = data ['created_at']
        self.updated_at = data ['updated_at']

#CLASSMETHODS WHICH ALLOW US TO MAKE QUIERIES TO GRAB STUFF ABOUT THE BOOK
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        result = connectToMySQL(DATABASE).query_db(query)
        all_books = []
        for db_row in result:
            book_instance = cls(db_row)
            all_books.append(book_instance)
        return all_books

    @classmethod
    def create(cls,data): #create a new book
        query = "INSERT INTO books (title, num_of_pages) VALUES (%(title)s,%(num_of_pages)s)"
        return connectToMySQL(DATABASE).query_db(query, data)