from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask_app.models import ninjas_model 

class Dojo: #creates the dojo class
    def __init__ (self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []


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

    @classmethod
    def create(cls,data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def read_one(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        if results:
            dojo_instance = cls(results[0]) 
            for db_row in results:
                ninja_data = {
                "id":db_row['ninjas.id'],
                "first_name":db_row['first_name'],
                "last_name":db_row['last_name'],
                "age":db_row['age'],
                "dojo_id":db_row['dojo_id'],
                "created_at":db_row['ninjas.created_at'],
                "updated_at":db_row['ninjas.updated_at']
            }
                this_ninja = ninjas_model.Ninja(ninja_data)
                dojo_instance.ninjas.append(this_ninja)
            return dojo_instance
        return results

    @classmethod
    def get_dojo_with_ninjas(cls,data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id =" \
        "dojo.id WHERE dojo.id = %(id)s;"
        result = connectToMySQL(DATABASE).query_db(query, data)
        dojo = cls(result[0])
        for db_row in result:
            ninja_data = {
                "id":db_row['ninja.id'],
                "first_name":db_row['ninja.first_name'],
                "last_name":db_row['ninja.last_name'],
                "age":db_row['ninja.age']
            }
            dojo.ninja.append(ninja.Ninja (ninja_data))
        return dojo