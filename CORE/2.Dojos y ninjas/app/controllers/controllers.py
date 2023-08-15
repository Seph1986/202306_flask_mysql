#Importaciones externas
from flask import render_template, redirect, request

#Importaciones locales
from app import app
from app.models.dojos import Dojo
from app.models.ninjas import Ninja


@app.route("/")
def home():

    return redirect("/dojo")


@app.route("/dojo/")
def landing():

    all_dojos = Dojo.get_all()

    return render_template("dojos_ninjas/dojos/landing.html", dojos = all_dojos)


@app.route("/dojo/new/", methods = ["POST"])
def new_dojo():

    form = request.form

    dojo_data = {
        "name" : form["name"]
    }
    print(f"---{dojo_data}---")

    Dojo.new_dojo(dojo_data)

    return redirect("/")


@app.route("/dojo/detail/<int:id>")
def dojo_detail(id):

    data = {
        "id" : id
    }
    
    dojo = Dojo.get_one(data)
    ninjas = Ninja.ninja_by_dojo(data)

    for ninja in ninjas:
        print(ninja.first_name)

    return render_template("dojos_ninjas/dojos/detail.html", dojo = dojo, ninjas = ninjas)


@app.route("/ninja/")
def landing_ninja():

    all_dojos = Dojo.get_all()

    return render_template("dojos_ninjas/ninjas/ninja.html", dojos = all_dojos)

@app.route("/ninja/add", methods=["POST"])
def add_ninja():

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

