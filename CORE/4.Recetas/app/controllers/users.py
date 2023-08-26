#Standard Imports
import os

#Importamos app
from app import app, bcrypt
from app.models.recipe import Recipe
#Models
from app.models.user import User
#Importamos Flask
from flask import flash, redirect, render_template, request, session, url_for

#Import Secret Key
secret_key = os.getenv("SECRET_KEY")


@app.route("/")
def landing():

    if "user" in session:
        return redirect(url_for("log_page"))
    
    

    return render_template("user/landing_page.html")


@app.route("/user/new/", methods=["POST"])
def create_user():        

    new_user = request.form
    print(new_user)

    
    if new_user["password"] != new_user["confirm_password"] or len(new_user["password"]) < 6:
        flash("Password error or min length 6","warning")
        return redirect(url_for("landing"))

    data ={
        "first_name": new_user["first_name"],
        "last_name": new_user["last_name"],
        "email": new_user["email"],
        "password": bcrypt.generate_password_hash(new_user["password"]),
        "confirm_password": bcrypt.generate_password_hash(new_user["confirm_password"]),
    }

    response = User.validation_data(data)

    if len(response) > 0:
        for message in response:
            flash(message,"warning")
        return redirect(url_for("landing"))


    User.create_user(data)
    print("---todo correcto---")

    flash("User created with success","warning")

    return redirect(url_for("landing"))


@app.route("/user/log/")
def log_page():

    if not "user" in session:
        return redirect(url_for("landing"))
    
    recipes = Recipe.get_all()
    print(recipes)


    return render_template("user/log.html",  recipes = recipes)

@app.route("/log/in/", methods=["POST"])
def check_if_exist():

    form = {
        "email" : request.form["email_log"],
        "password" : request.form["password_log"]
    }

    user = User.get_by_email(form["email"])

    if not user:
        flash("log error","warning")
        return redirect(url_for("landing"))
    
    response = bcrypt.check_password_hash(user.password, form["password"])

    if response:
        session["user"] = {
        "id": user.id,
        "email": user.email,
        "first_name": user.first_name,
        "last_name": user.last_name }

        return redirect(url_for("log_page"))
    
    flash("log error","warning")
    return redirect(url_for("landing"))


@app.route("/user/log/out/")
def log_out():

    session.clear()

    return redirect(url_for("landing"))