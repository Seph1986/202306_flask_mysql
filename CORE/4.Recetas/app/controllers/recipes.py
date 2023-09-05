#Standard Imports
import os

#Importamos app
from app import app
#Models
from app.models.recipe import Recipe
#Importamos Flask
from flask import flash, redirect, render_template, request, session, url_for

#Import Secret Key3
secret_key = os.getenv("SECRET_KEY")


@app.route("/recipe/add/")
def show_add_form():

    if not "user" in session:
        return redirect(url_for("landing"))


    return render_template("/recipe/add_form.html")

@app.route("/recipe/add/process/", methods=["POST"])
def add_recipe():
    
    recipe_data = request.form
    print(recipe_data)
    form = Recipe.validation_data(recipe_data)

    if len(form) > 0:
        for error in form:
            flash(error, "warning")

    print(session["user"])
    
    data = {
        "id": recipe_data["id"],
        "name": recipe_data["name"],
        "description": recipe_data["description"],
        "under_30": recipe_data["under_30"],
        "instruction": recipe_data["instruction"],
        "date_cooked": recipe_data["date_cooked"],
    }

    Recipe.add_recipe(data)
    flash("Recipe added","warning")

    return redirect(url_for("show_add_form"))

@app.route("/recipe/details/<int:id>/")
def recipe_details(id):

    if not "user" in session:
        return redirect(url_for("landing"))

    print(id)

    recipe = Recipe.get_by_id(id)

    return render_template("recipe/details.html", recipe = recipe)


@app.route("/recipe/edit/<int:id>/")
def recipe_edit(id):

    if not "user" in session:
        return redirect(url_for("landing"))
    
    recipe = Recipe.get_by_id(id)

    return render_template("recipe/edit_form.html", recipe = recipe)

@app.route("/recipe/edit/process/", methods=["post"])
def process_edit():
    
    recipe_data = request.form
    print(recipe_data)
    form = Recipe.validation_data(recipe_data)

    if len(form) > 0:
        for error in form:
            flash(error, "warning")
    
    data = {
        "id": recipe_data["id"],
        "name": recipe_data["name"],
        "description": recipe_data["description"],
        "under_30": recipe_data["under_30"],
        "instruction": recipe_data["instruction"],
        "date_cooked": str(recipe_data["date_cooked"]),
        "email": session["user"]["email"]
    }

    Recipe.edit(data)
    flash("Edited Recipe","warning")

    
    return redirect(url_for("recipe_edit", id = data["id"]))


@app.route("/recipe/delete/<int:id>/")
def recipe_delte(id):

    Recipe.delete(id)

    return redirect(url_for("log_page"))