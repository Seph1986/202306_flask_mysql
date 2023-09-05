from app.config.mysqlconnection import connectToMySQL
from app.models.ninjas import Ninja

class Dojo:

    def __init__(self, data) -> None:
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []

    def __str__(self) -> str:
       return f"""Atributos de Dojo id = {self.id} name = {self.name} created_at:
       {self.created_at}, updated_at = {self.updated_at} y {self.ninjas}""" 


    @classmethod
    def new_dojo(cls,data):

        """
        Agrega un nuevo dojo a la base de datos.

        Parámetros:
            - cls: La clase que invoca este método.
            - data: Un diccionario con los datos del dojo a agregar. Se espera
              que tenga una clave "name" que corresponda al nombre del dojo.

        No hay valor de retorno.
        """

        query = "INSERT INTO dojos(name) VALUES (%(name)s);"
        
        connectToMySQL("ninjas_dojos").query_db(query, data)

    
    @classmethod
    def get_all(cls):

        """
        Obtiene todos los dojos almacenados en la base de datos.

        Parámetros:
            - cls: La clase que invoca este método.

        Valor de retorno:
            - Una lista de objetos tipo Dojo, que representan los dojos 
            obtenidos de la base de datos.
        """

        dojos = []

        query = "SELECT * FROM dojos"

        response = connectToMySQL("ninjas_dojos").query_db(query)

        for dojo in response:
            dojos.append(cls(dojo))

        print(f"----{dojos}----")

        return dojos

    
    @classmethod
    def get_one(cls, data):

        """
        Obtiene un único dojo junto con todos sus ninjas de la base de datos,
          dado un ID de dojo.

        Parámetros:
            - cls: La clase que invoca este método.
            - data: Un diccionario que contiene el ID del dojo a obtener.

        Valor de retorno:
            - Un objeto tipo Dojo, que representa el dojo obtenido de la base
              de datos, incluidos todos los ninjas asociados.
        """

        query = """SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = 
        ninjas.dojo_id WHERE dojos.id = %(id)s"""

        result = connectToMySQL("ninjas_dojos").query_db(query,data)
        dojo = cls(result[0])

        all_ninjas = []
        for row_db in result:
            print("--Fila",row_db)

            ninja_data = {
                "id" : row_db["ninjas.id"],
                "first_name" : row_db["first_name"],
                "last_name" : row_db["last_name"],
                "age" : row_db["age"],
                "created_at" : row_db["ninjas.created_at"],
                "updated_at" : row_db["ninjas.updated_at"],
                "dojo_id" : row_db["id"]
            }

            ninja_instance = Ninja(ninja_data)
            all_ninjas.append(ninja_instance)

        dojo.ninjas = all_ninjas
        print(dojo)

        return dojo