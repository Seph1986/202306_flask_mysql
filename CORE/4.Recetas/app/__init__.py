#Standard librarys
import os

#Importamos flask
from flask import Flask
from flask_bcrypt import Bcrypt 

# Python-dotenv
from dotenv import load_dotenv

#Instanciamos Flask
app = Flask(__name__)

#Instanciamos Byctrypt
bcrypt = Bcrypt(app) 

# Secret key
app.secret_key = os.getenv("SECRET_KEY")

# Load Python-dotenv
load_dotenv()