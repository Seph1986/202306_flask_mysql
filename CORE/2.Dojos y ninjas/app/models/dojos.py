from app.config.mysqlconnection import connectToMySQL

class Dojo:

    def __init__(self, data) -> None:
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []

    def __str__(self) -> str:
        f"""Atributos de Dojo id = {self.id} name = {self.name} created_at:
        {self.created_at} y updated_at = {self.updated_at}""" 


    @classmethod
    def new_dojo(cls,data):

        query = "INSERT INTO dojos(name) VALUES (%(name)s);"
        
        connectToMySQL("ninjas_dojos").query_db(query, data)

    
    @classmethod
    def get_all(cls):

        dojos = []

        query = "SELECT * FROM dojos"

        response = connectToMySQL("ninjas_dojos").query_db(query)

        for dojo in response:
            dojos.append(cls(dojo))

        print(f"----{dojos}----")

        return dojos

    
    @classmethod
    def get_one(cls, data):

        query = "SELECT * FROM dojos WHERE id = %(id)s"

        result = connectToMySQL("ninjas_dojos").query_db(query, data)

        return cls(result[0])