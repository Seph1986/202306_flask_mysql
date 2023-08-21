#IMPORTACIONES
from flask import render_template, redirect, flash, url_for, session, request
from app import app
from app.models.email import Email

#SECRET KEY
app.secret_key = "super secret key"


@app.route("/")
def landing():

    return render_template("form/landing.html")


@app.route("/add/", methods=["POST"])
def add_email():

    data = {
        "email": request.form["email"]
    }

    response = Email.validate_form(data)

    if not response:
        return redirect("/")
    
    
    print(data)
    Email.add_email(data)


    return redirect(url_for("email_data"))


@app.route("/data/")
def email_data():

    emails = Email.get_all()
    
    for email in emails:
        print(email)

    

    return render_template("form/data.html", emails = emails)