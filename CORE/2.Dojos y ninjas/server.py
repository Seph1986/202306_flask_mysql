from app import app
from app.controllers.controllers import *

#Inciamos el servidor en modo debug
if __name__=="__main__":
    app.run(debug=True)