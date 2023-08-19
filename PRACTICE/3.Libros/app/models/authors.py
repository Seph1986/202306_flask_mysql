#Config
from app.config.mysqlconnection import connectToMySQL

#Models
from app.models.books import Book

class Author:

    def __init__(self,data:dict) -> None:
        self.id = data["id"]
        self.name = data["name"]
        self.favorite_books: list= []
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]


    def __str__(self) -> str:
        return f"""Atributos de la clase Author : (id = {self.id}, 
        name = {self.name}, libros favoritos = {self.favorite_books},
        created_at = {self.created_at},updated_at = {self.updated_at})"""
    

    @classmethod
    def new_author(cls,data:dict):

        """
        Función estática que crea un nuevo autor en la base de datos.

        Parameters:
            - cls (class): La clase desde la cual se llama
            - data (dict): Un diccionario con los datos del autor a ser 
            creado. Debe contener el nombre del autor con la key "name"

        Returns:
            None

        """

        query = """INSERT INTO authors(name) VALUES(%(name)s)"""

        connectToMySQL("authors_books").query_db(query,data)

    @classmethod
    def all_authors(cls):

        """
        Función estática que obtiene todos los autores de la base de datos.

        Parameters:
            - cls (class): La clase desde la cual se llama.

        Returns:
            list: Lista de diccionarios que representan a todos los autores en
            la base de datos. Cada diccionario contiene los detalles de un autor.

        """

        query = "SELECT * FROM authors"

        result = connectToMySQL("authors_books").query_db(query)

        return result
    
    
    @classmethod
    def get_author(cls,data):

        query = """SELECT * FROM authors
        LEFT JOIN authors_books ON authors.id = authors_books.author_id
        LEFT JOIN books ON books.id = authors_books.book_id
        WHERE authors.id = %(id)s;"""

        response = connectToMySQL("authors_books").query_db(query, data)

        author = cls(response[0])

        for row in response:
            if row["book_id"] is not None:

                book_data={
                    "id":row["books.id"],
                    "title":row["title"],
                    "num_of_pages":row["num_of_pages"],
                    "created_at":row["books.created_at"],
                    "updated_at":row["books.updated_at"]
                }
                author.favorite_books.append(Book(book_data))

        print(author)
        return author
    

    @classmethod
    def add_book_to_favorite(cls,data: dict):

        query = """INSERT INTO authors_books(author_id, book_id)
        VALUES ( %(author_id)s, %(book_id)s )"""

        return connectToMySQL("authors_books").query_db(query,data)
    

    @classmethod
    def author_that_hasnt_selected(cls, data: dict):

        query="""
        SELECT * FROM authors
        WHERE authors.id NOT IN(
            SELECT author_id FROM authors_books 
            WHERE book_id = %(id)s
        )
        """

        result = connectToMySQL("authors_books").query_db(query,data)
        print(result)

        authors_no_liked: list = []

        for author in result:
            authors_no_liked.append(cls(author))

        print(authors_no_liked)
        return authors_no_liked