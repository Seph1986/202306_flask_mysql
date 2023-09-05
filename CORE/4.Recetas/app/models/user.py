#Standard Imports
import re

#Import mysql conection
from app.config.mysql_connection import connect_to_mysql


class User:

    def __init__(self, data: dict) -> None:
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.password = data["password"]
        self.recipes = []
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    def __str__(self) -> str:
        return f"""{self.id},{self.first_name},{self.last_name},{self.email},
        {self.recipes},{self.created_at},{self.updated_at }"""
        

    @classmethod
    def get_all(cls):

        all_users = []

        query = "SELECT * FROM users"

        response = connect_to_mysql().query_db(query)

        for user in response:
            all_users.append(cls(user))

        return all_users

    @classmethod
    def create_user(cls,data: dict):
        
        query="""
        INSERT INTO users(first_name,last_name,email,password)
        VALUES(%(first_name)s,%(last_name)s,%(email)s,%(password)s)
        """

        connect_to_mysql().query_db(query,data)


    @classmethod
    def get_by_email(cls, email):


        query = """
        SELECT * FROM users WHERE email = %(email)s
        """

        data = {
            "email": email
        }

        result = connect_to_mysql().query_db(query,data)

        if result:
            return cls(result[0])

        return None

    
    @staticmethod
    def validation_data(data):

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

        errors = []
        print(data)
        
        
        if len(data["first_name"]) < 4:
            errors.append("Invalid name")

        if len(data["last_name"]) < 2:
            errors.append("Invalid last name")

        if not EMAIL_REGEX.match(data["email"]):
            errors.append("Invalid email")
        
        if User.get_by_email(data["email"]): 
            errors.append("Invalid email")
        

        return errors