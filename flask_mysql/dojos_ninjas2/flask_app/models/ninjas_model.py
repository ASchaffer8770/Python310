from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE


class Ninja: #creates the ninja class
    def __init__ (self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']

#add dojo methods below
    @classmethod
    def get_all(cls): #get all method for dojos
        query = "SELECT * FROM ninjas;"
        result = connectToMySQL(DATABASE).query_db(query)
        all_ninjas = []
        for row_from_db in result:
            ninja_instance = cls(row_from_db)
            all_ninjas.append(ninja_instance)
        return all_ninjas

    @classmethod
    def create(cls,data): #create ninja
        query = "INSERT INTO dojos (first_name, last_name, age, dojo_id) VALUES (%(first_name)s,%(last_name)s,%(age)s,%(dojo_id)s)"
        return connectToMySQL(DATABASE).query_db(query,data)

    @classmethod
    def update(cls,data): #update ninja
        query = "UPDATE ninjas SET first_name=%(first_name)s, last_name=%(last_name)s, age=%(age)s" \
            "WHERE id = %(id)s"