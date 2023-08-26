#Import mysql conection
from app.config.mysql_connection import connect_to_mysql

#Import user model
from app.models.user import User

class Recipe:

    def __init__(self, data: dict) -> None:
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.under_30 = data["under_30"]
        self.instruction = data["instruction"]
        self.date_cooked = data["date_cooked"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
        self.user_instance = None


    @classmethod
    def get_all(cls):

        all_recipes = []

        query = """SELECT * FROM recipes
        LEFT JOIN users
        ON users.id = recipes.user_id;"""

        result = connect_to_mysql().query_db(query)

        for recipe in result:
            print(recipe)
            instancia = cls(recipe)

            data = {
            "id" : recipe["users.id"],
            "first_name" : recipe["first_name"],
            "last_name" : recipe["last_name"],
            "email" : recipe["email"],
            "password" : recipe["password"],
            "created_at" : recipe["users.created_at"],
            "updated_at" : recipe["users.updated_at"],
            }

            instancia.user_instance = User(data)
            print(instancia.user_instance)
            all_recipes.append(instancia)
        

        print(all_recipes)
        return all_recipes
    
    @classmethod
    def get_by_id(cls, id):

        query = """SELECT * FROM recipes
        LEFT JOIN users
        ON users.id = recipes.user_id WHERE recipes.id = %(id)s"""

        data_id = {
            "id": id
        }

        result = connect_to_mysql().query_db(query, data_id)

        recipe_instance = cls(result[0])

        data = {
            "id" : result[0]["users.id"],
            "first_name" : result[0]["first_name"],
            "last_name" : result[0]["last_name"],
            "email" : result[0]["email"],
            "password" : result[0]["password"],
            "created_at" : result[0]["users.created_at"],
            "updated_at" : result[0]["users.updated_at"],
            }
        
        recipe_instance.user_instance = User(data)

        return recipe_instance
    
    

    @classmethod
    def add_recipe(cls, data: dict):
        
        query = """
        INSERT INTO recipes
        (name,description,under_30,instruction,date_cooked,user_id)
        VALUES
        (%(name)s,%(description)s,%(under_30)s,%(instruction)s,%(date_cooked)s,
        (SELECT id FROM users WHERE id = %(id)s))"""

        connect_to_mysql().query_db(query,data)

    
    @classmethod
    def edit(cls, data: dict):

        query= """UPDATE recipes
        SET name = %(name)s,description = %(description)s,
        under_30 = %(under_30)s,instruction = %(instruction)s, date_cooked = 
        %(date_cooked)s
        WHERE id = %(id)s
        """

        return connect_to_mysql().query_db(query,data)
    
    @classmethod
    def delete(cls, id):

        query = """DELETE FROM recipes WHERE id = %(id)s"""

        data = {
            "id": id
        }

        connect_to_mysql().query_db(query, data)

    
    @staticmethod
    def validation_data(data: dict):
    
        messages = []

        if len(data["name"]) < 4:
            messages.append("Name must have 4 character")
        if len(data["description"]) < 12:
            messages.append("Name must have 12 character")
        if len(data["instruction"]) < 10:
            messages.append("Name must have 12 character")
        if not data["date_cooked"]:
            messages.append("Must select a date")

        return messages
