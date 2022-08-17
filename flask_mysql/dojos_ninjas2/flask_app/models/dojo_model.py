from flask_app.config.mysqlconnection import connectToMySQL
DATABASE = "dojos_and_ninjas_schema"

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
        all_dojos = []
        for row_from_db in result:
            dojo_instance = cls(row_from_db)
            all_dojos.append(dojo_instance)
        return all_dojos