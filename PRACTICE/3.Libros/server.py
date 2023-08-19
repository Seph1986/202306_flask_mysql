#Importamos app de app
from app import app

from app.controllers.author_cont import *
from app.controllers.book_contr import *

# Iniciamos nuestro servidor
if __name__ == "__main__":
    app.run(debug=True)