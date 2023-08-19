#Importaciones externas
from flask import render_template, redirect, url_for ,request

#Importaciones locales
from app import app
from app.models.authors import Author
from app.models.books import Book


@app.route("/")
def landing():

    return redirect(url_for("authors"))


@app.route("/authors/")
def authors():

    authors = Author.all_authors()

    return render_template("authors/home_page.html", authors = authors)

@app.route("/authors/add", methods=["POST"])
def add_author():

    data = request.form

    author_info = {
        "name" : data["name"],
    }

    Author.new_author(author_info)

    return redirect(url_for("authors"))


@app.route("/author/<int:id>/")
def author_info(id):
    
    data={
        "id":id,
    }

    context = {
        "author": Author.get_author(data),
        "books": Book.books_with_no_likes(data)
        }

    return render_template("authors/author_info.html", **context)

@app.route("/author/add/favorite/<int:id>", methods=["POST"])
def add_favorite_book(id):

    data = {
        "author_id": id,
        "book_id": request.form["book_id"]
    }

    Author.add_book_to_favorite(data)
    return redirect(url_for("author_info", id = data["author_id"]))

