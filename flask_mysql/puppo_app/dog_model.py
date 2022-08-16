from mysqlconnection import connectToMySQL
DATABASE = "dogs_schema" #this is the db we are accessing and using for queries

class Dog:
    def __init__(self, data): #takes in itself and Data, THIS is how we can create CRUD
        self.id = data['id']
        self.name = data['name']
        self.breed = data['breed']
        self.color = data['color']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

#READ ALL METHOD
    @classmethod
    def get_all(cls): #This is where queries go to controll the dog_schema DB
        query = "SELECT * FROM dogs;" #query where we select all dogs
        results = connectToMySQL(DATABASE).query_db(query) #Holds list of results that come back from db has to be exact name of schema which is imported at top of page
        #line 16 connects to db and passes in just the query
        # print (results)
        all_dogs = []
        for row_from_db in results:
            dog_instance = cls(row_from_db) #references class we are in  and instanciated a dictionary
            all_dogs.append(dog_instance)
        return all_dogs #this loop creates an instance from the class and turns a row into displayable data

    #READ ONE
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dogs WHERE id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query,data)
        if results:
            dog_instance = cls(results[0])
            return dog_instance
        return results


    #CREATE A DOG
    @classmethod
    def create(cls, data):
        query = "INSERT INTO dogs (name, color, breed) VALUES (%(name)s, %(color)s, %(breed)s);"
        return connectToMySQL(DATABASE).query_db(query, data)

    #UPDATE A DOG
    @classmethod
    def update(cls, data):
        query = "UPDATE dogs SET name = %(name)s, color = %(color)s, breed = %(breed)s" \
            "WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)

    #REMOVE AN ENTRY (DELETE)
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM dogs WHERE id = %(id)s;"
        return connectToMySQL(DATABASE).query_db(query, data)