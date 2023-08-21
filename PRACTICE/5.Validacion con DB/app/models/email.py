#Importamos Flask
from flask import flash

#Coneccion con MySQL
from app.config.pymysql import connect_to_my_sql

#Importamos Expresiones Regulares
import re

#Expresion regular
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class Email:

    def __init__(self, data: dict) -> None:
        self.id = data["id"]
        self.email_adress = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


    def __str__(self) -> str:
        return f"""email = {self.email_adress}, created at = {self.created_at}
        updated at = {self.updated_at}"""
    
    
    @classmethod
    def add_email(cls, data: dict):
        
        query = """INSERT INTO users_emails(email)
        VALUES(%(email)s)"""

        connect_to_my_sql("emails").query_db(query,data)
        flash(f"Email: {data['email']} added successfully")


    @classmethod
    def get_all(cls):

        all_adresses = []

        query = "SELECT * FROM users_emails"

        response = connect_to_my_sql("emails").query_db(query)

        for adress in response:
            all_adresses.append(cls(adress))

        return all_adresses
    

    @classmethod
    def delete_address(cls, data):

        query = "DELETE FROM users_emails WHERE id = %(id)s"

        connect_to_my_sql("emails").query_db(query,data)


    @staticmethod
    def validate_form(form):
        validation = True

        if not EMAIL_REGEX.match(form["email"]):
            validation = False
            flash("Invalid email","warning")

        all_adressess = Email.get_all()
        print(f"---{all_adressess}---")

        for address in all_adressess:
            if address.email_adress == form["email"]:
                validation = False
                flash("Email already exist","warning")

        return validation

    