from flask import render_template, redirect, request

from app.models.users import User
from app import app


@app.route("/")
def home():

    """Redirige a nuestra direccion "/user/" """

    return redirect("/user")


@app.route("/user/")
def all_users():

    """
    Esta función maneja la ruta "/user/" y devuelve todos los usuarios.

    Returns:
        template: La plantilla "friends.html" renderizada con el argumento friends.
    """

    friends = User.get_all()
    for f in friends:
        print(f)
    
    return render_template("friends.html", friends = friends)


@app.route("/user/new/")
def user_form():

    """Esta funcion maneja la ruta "/user/new" 

    Returns:
        template: La plantilla "new_friends.html"
    """

    return render_template("new_friend.html")


@app.route("/user/form/", methods=["POST"])
def add_user():

    """
    Esta función maneja la ruta "/user/form/" y se utiliza para agregar un nuevo usuario.

    Returns:
        redirect: Redirecciona a la ruta "/user/" después de agregar el usuario.
    """

    form = request.form

    data_filled = {
        "first_name": form["first_name"],
        "last_name": form["last_name"],
        "occupation": form["occupation"]
    }

    print(f"--Diccioanrio-- {data_filled}")

    User.add_user(data_filled)

    return redirect("/user/")