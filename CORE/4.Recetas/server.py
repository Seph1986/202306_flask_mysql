#Importaciones locales
from app import app

#Controladores
from app.controllers.users import *
from app.controllers.recipes import *

#Iniciamos servidor
if __name__ == "__main__":
    app.run(debug=True)