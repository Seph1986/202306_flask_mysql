#Importaciones externas
from flask import render_template, redirect, request

#Importaciones locales
from app import app
from app.models.dojos import Dojo
from app.models.ninjas import Ninja


@app.route("/")
def home():

    """
    Redirige a la página principal del Dojo.

    Parámetros:
        - Ninguno.

    Valor de retorno:
        - Redirecciona al usuario a la URL "/dojo".
    """

    return redirect("/dojo")


@app.route("/dojo/")
def landing():

    """
    Página principal que muestra todos los dojos.

    Parámetros:
        - Ninguno.

    Valor de retorno:
        - Renderiza el template "dojos_ninjas/dojos/landing.html" con una variable
      llamada "dojos" que contiene todos los dojos existentes en la base de datos.

    Requisitos:
        - Asegúrate de tener definida una función llamada "get_all" en la clase 
    "Dojo" que devuelva todos los dojos existentes en la base de datos.

    Ejemplo de uso:
        - Navegar a la URL "/dojo/" para ver la página principal que muestra todos
    los dojos existentes.

    Nota:
        - El template "dojos_ninjas/dojos/landing.html" debe contener el código 
    necesario para mostrar los dojos recibidos en la variable "dojos".
    """

    all_dojos = Dojo.get_all()

    return render_template("dojos_ninjas/dojos/landing.html", dojos = all_dojos)


@app.route("/dojo/new/", methods = ["POST"])
def new_dojo():

    """
    Crea un nuevo dojo.

    Parámetros:
        - Ninguno.

    Valor de retorno:
        - Redirecciona al inicio ("/") después de crear el nuevo dojo.

    Requisitos:
        - Esta función debe ser llamada a través de una solicitud POST.

    Ejemplo de uso:
        - Enviar una solicitud POST a la URL "/dojo/new/" con los datos del 
    formulario para crear un nuevo dojo.
        - Después de crear exitosamente el dojo, se redireccionará al usuario a 
    la página de inicio ("/").

    Nota:
        - Asegúrate de que el formulario incluya un campo llamado "name" para capturar el nombre del dojo.
        - Asegúrate de tener definida una función llamada "new_dojo" en la clase 
    "Dojo" que cree un nuevo dojo en la base de datos utilizando los datos 
    proporcionados.
    """

    form = request.form

    dojo_data = {
        "name" : form["name"]
    }
    print(f"---{dojo_data}---")

    Dojo.new_dojo(dojo_data)

    return redirect("/")


@app.route("/dojo/detail/<int:id>")
def dojo_detail(id):

    """
    Muestra los detalles de un dojo específico.

    Parámetros:
        - id: Un entero que representa el identificador único del dojo.

    Valor de retorno:
        - Una página HTML que muestra los detalles del dojo.

    Ejemplo de uso:
        - Acceder a la URL "/dojo/detail/1" en el navegador para ver los detalles
      del dojo con id 1.

    Nota:
        - Asegúrate de tener una plantilla HTML llamada "dojos_ninjas/dojos/detail.html" que se utilice para renderizar la página.
        - Asegúrate de tener definida una función llamada "get_one" en la clase 
    "Dojo" que obtenga un dojo específico de la base de datos utilizando su 
    id.
    """

    data = {
        "id" : id
    }
    
    dojo = Dojo.get_one(data)
    

    return render_template("dojos_ninjas/dojos/detail.html", dojo = dojo)


@app.route("/ninja/")
def landing_ninja():

    """
    Muestra una página que lista todos los dojos y sus respectivos ninjas.

    Parámetros:
        - Ninguno.

    Valor de retorno:
        - Una página HTML que muestra todos los dojos y sus ninjas.

    Ejemplo de uso:
        - Acceder a la URL "/ninja/" en el navegador para ver la lista de 
        dojos y ninjas.

    Nota:
        - Asegúrate de tener una plantilla HTML llamada 
        "dojos_ninjas/ninjas/ninja.html" que se utilice para renderizar la 
        página.
        - Asegúrate de tener definida una función llamada "get_all" en la 
        clase "Dojo" que obtenga todos los dojos de la base de datos.
    """

    all_dojos = Dojo.get_all()

    return render_template("dojos_ninjas/ninjas/ninja.html", dojos = all_dojos)


@app.route("/ninja/add", methods=["POST"])
def add_ninja():

    """
    Agrega un nuevo ninja a la base de datos.

    Parámetros:
        - Ninguno.

    Valor de retorno:
        - Redirecciona al inicio ("/") después de agregar exitosamente al 
        ninja.

    Ejemplo de uso:
        - Enviar una solicitud POST a "/ninja/add" con los siguientes datos en
          el cuerpo de la solicitud:
        {
            "first_name": "John",
            "last_name": "Doe",
            "age": 25,
            "dojo": 1
        }

    Nota:
        - Asegúrate de tener una columna equivalente para cada clave en el
          diccionario "data" utilizado en la función.
    """

    new_ninja = request.form
    print(new_ninja)

    data = {
        "first_name" : new_ninja["first_name"],
        "last_name" : new_ninja["last_name"],
        "age": new_ninja["age"],
        "dojo_id": new_ninja["dojo"]
    }

    print(data)

    Ninja.new_ninja(data)
    

    return redirect("/")

