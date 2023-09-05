#Importaciones
from app.config.mysqlconnection import connectToMySQL

#Clase de usuarios
class User:

    def __init__(self, data) -> None:
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.ocupation = data["occupation"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    def __str__(self) -> str:
        
        return f"Datos de la instancia Users: first_name: {self.first_name},last_name: {self.last_name}, occupation: {self.ocupation}"
    
    @classmethod
    def get_all(cls):

        """
        Método de clase que devuelve una lista de objetos de la clase actual.
    
        Parámetros:
            - cls: La clase actual.
        
        Retorna:
            - all_users: Lista de objetos de la clase actual.
        """


        all_users = []
        
        query = "SELECT * FROM friends"
        friends = connectToMySQL("first_flask").query_db(query)

        for friend in friends:
            all_users.append(cls(friend))

        return all_users

    @classmethod
    def add_user(cls,data):

        """
        Método de clase que agrega un nuevo usuario a la base de datos.

        Parámetros:
            - cls: La clase actual.
            - data: Un diccionario con los datos del usuario a agregar, incluyendo 'first_name', 'last_name' y 'occupation'.

        Retorna:
            - None
        """

        query = "INSERT INTO friends(first_name,last_name,occupation) VALUES(%(first_name)s, %(last_name)s, %(occupation)s);"
        
        return connectToMySQL("first_flask").query_db(query, data)