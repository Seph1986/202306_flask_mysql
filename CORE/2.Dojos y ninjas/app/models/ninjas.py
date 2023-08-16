from app.config.mysqlconnection import connectToMySQL

class Ninja:

    def __init__(self, data) -> None:
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.dojo_id = data["dojo_id"]

    def __str__(self) -> str:
        f"""Atributos de Ninja id = {self.id}, first_name = 
        {self.first_name}, last_name = {self.last_name}, age = {self.age},
        created_at = {self.created_at}, updated_at = {self.updated_at},
        dojo = {self.dojo_id}"""

    
    @classmethod
    def new_ninja(cls,data):

        """
        """

        query = """INSERT INTO ninjas(first_name,last_name,age,dojo_id)
        VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s)"""

        connectToMySQL("ninjas_dojos").query_db(query, data)

    @classmethod
    def ninja_by_dojo(cls, data):

        """
        Obtiene una lista de todos los ninjas pertenecientes a un dojo 
        específico, dado un ID de dojo.

        Parámetros:
            - cls: La clase que invoca este método.
            - data: Un diccionario que contiene el ID del dojo.

        Valor de retorno:
            - Una lista de objetos tipo Ninja, que representan los ninjas 
            asociados al dojo.
        """

        ninjas = []

        query = """SELECT * FROM ninjas WHERE dojo_id = %(id)s"""

        result = connectToMySQL("ninjas_dojos").query_db(query,data)

        for ninja in result:
            ninjas.append(cls(ninja))

        return ninjas