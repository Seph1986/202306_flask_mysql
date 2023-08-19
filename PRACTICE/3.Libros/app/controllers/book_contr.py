#Importaciones externas
from flask import render_template, redirect, url_for ,request

#Importaciones locales
from app import app
from app.models.books import Book
from app.models.authors import Author

@app.route("/books/")
def books_landing():

    books=Book.all_books()

    return render_template("books/landing.html", books = books)

@app.route("/books/add/", methods=["POST"])
def new_book():

    result = request.form

    book_data = {
        "title" : result["title"],
        "num_of_pages" : result["num_of_pages"]
    }

    Book.new_book(book_data)

    return redirect(url_for("books_landing"))

@app.route("/book/<int:id>/")
def book_info(id):
    
    print(f"---{id}---")

    data = {
        "id" : id
    }

    context = {
        "book": Book.get_book(data),
        "authors": Author.author_that_hasnt_selected(data)
        }


    return render_template("books/book_info.html", **context)


@app.route("/book/add/favorite/<int:id>", methods=["POST"])
def add_favorite_author(id):    

    data = {
        "book_id": id,
        "author_id": request.form["author_id"]
    }

    Book.add_author_to_favorite(data)
    return redirect(url_for("book_info", id = data["book_id"]))
