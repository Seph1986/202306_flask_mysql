#Standard Imports
import os

#Importamos app
from app import app, bcrypt

#Models
from app.models.user import User

#Importamos Flask
from flask import Flask,render_template, redirect,flash, url_for, session, request

#Import Secret Key
secret_key = os.getenv("SECRET_KEY")


@app.route("/")
def landing():

    if "user" in session:
        flash("You are loged","info")
        return redirect(url_for(log_page))

    return render_template("user/landing_page.html")


@app.route("/user/new/", methods=["POST"])
def create_user():        

    new_user = request.form

    if new_user["password"] != new_user["confirm_password"] or len(new_user["password"]) < 6:
        flash("Password error or min length 6","warning")
        return redirect(url_for("landing"))

    response = User.validation_data(new_user)

    if len(response) > 0:
        for message in response:
            flash(message,"warning")
        return redirect(url_for("landing"))


    data ={
        "first_name": new_user["first_name"],
        "last_name": new_user["last_name"],
        "email": new_user["email"],
        "password": bcrypt.generate_password_hash(new_user["password"]),
        "confirm_password": bcrypt.generate_password_hash(new_user["confirm_password"]),
    }


    session["user"] = {
        "email": data["email"],
        "first_name": data["first_name"],
        "last_name": data["last_name"] }
    

    User.create_user(data)

    print("---todo correcto---")

    

    return redirect(url_for("log_page"))


@app.route("/user/log/")
def log_page():

    if not "user" in session:
        return redirect(url_for("landing"))


    return render_template("user/log.html")

@app.route("/log/in/", methods=["POST"])
def check_if_exist():

    form = {
        "email" : request.form["email_log"],
        "password" : request.form["password_log"]
    }

    user = User.get_by_email(form)

    if not user:
        flash("log error","warning")
        return redirect(url_for("landing"))
    
    response = bcrypt.check_password_hash(user.password, form["password"])

    if response:
        session["user"] = {
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