from flask import render_template, redirect, request

from app.models.users import User
from app import app


@app.route("/")
def home():

    """Redirige a nuestra direccion "/user/" """

    return redirect("/friends")


@app.route("/friends/")
def all_users():

    """
    Esta función maneja la ruta "/user/" y devuelve todos los usuarios.

    Returns:
        template: La plantilla "friends.html" renderizada con el argumento friends.
    """

    friends = User.get_all()
    for f in friends:
        print(f)
    
    return render_template("friends/all.html", friends = friends)


@app.route("/friends/new/")
def user_form():

    """Esta funcion maneja la ruta "/user/new" 

    Returns:
        template: La plantilla "new_friends.html"
    """

    return render_template("friends/new.html")


@app.route("/friends/form/", methods=["POST"])
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

    return redirect("/friends/")

@app.route("/friends/detail/<int:id>")
def show_details(id):

    """
    Esta función muestra los detalles de un amigo según su ID.

    Args:
        id (int): El ID del amigo.
    Returns:
        render_template: Renderiza la plantilla HTML con los detalles del amigo.
    """

    data = {
        "id" : id
    }
    
    friend = User.get_one(data)

    print(f"---{id}---")
    print(friend)

    return render_template("/friends/details.html", friend = friend)


@app.route("/friends/edit/<int:id>")
def edit_friend(id):

    data = {
        "id": id
    }

    friend = User.get_one(data)
    print(f"---{id}---")

    return render_template("/friends/edit.html", friend = friend)

@app.route("/friends/edit/process/<int:id>/", methods=["POST"])
def process_form(id):

    edited_values = request.form

    data_for_edit = {
        "id" : edited_values["id"],
        "first_name" : edited_values["first_name"],
        "last_name" :edited_values["last_name"],
        "occupation" :edited_values["occupation"]
    }
    print(edited_values)
    print(data_for_edit)

    User.edit_user(data_for_edit)

    return redirect("/friends/")

@app.route("/friends/delete/<int:id>/")
def delete_user(id):

    data = {
        "id" : id
    }

    print("persona borrada con id:", data)

    User.delete_user(data)
    
    return redirect("/friends/")