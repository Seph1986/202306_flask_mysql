#Importaciones externas
from flask import render_template, redirect, session, request

#Importaciones locales
from app import app
from app.models.surveys import Survey

@app.route("/")
def landing():


    return render_template("landing.html")


@app.route("/form/", methods = ["POST"])
def form_recive():

    print(request.form)
    if not Survey.validate_data(request.form):
        return redirect("/")

    keys = ["user_name","location","language","comment"]

    for key in keys:
        session[key] = request.form[key]
    

    print(session["user_name"],session["location"],session["language"],session["comment"] )
    

    return redirect("/result/")


@app.route("/result/")
def result():

    return render_template("info.html")


@app.route("/reset/")
def reset_user():

    keys = ["user_name","location","language","comment"]

    for key in keys:
        del session[key]

    return redirect("/")


