from app.config.mysqlconnection import connectToMySQL

#Models
from app.models import authors


class Book:

    def __init__(self, data:dict) -> None:
        self.id = data["id"]
        self.title = data["title"]
        self.num_of_pages = data["num_of_pages"]
        self.favorite_authors: list = []
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def new_book(cls,data:dict):

        """
        Función estática que crea un nuevo libro en la base de datos.

        Parameters:
            - cls (class): La clase desde la cual se llama
            - data (dict): Un diccionario con los datos del libro a ser 
            creado. Debe contener el titulo del libro con la key "name" y el
            numero de paginas con la key "num_of_pages"

        Returns:
            None

        """

        query = """INSERT INTO books(title,num_of_pages) 
        VALUES(%(title)s, %(num_of_pages)s)"""

        connectToMySQL("authors_books").query_db(query,data)


    @classmethod
    def all_books(cls):

        """
        Función estática que obtiene todos los libros de la base de datos.

        Parameters:
            - cls (class): La clase desde la cual se llama.

        Returns:
            list: Lista de diccionarios que representan a todos los libros en
            la base de datos. Cada diccionario contiene los detalles de un libro.

        """

        query = "SELECT * FROM books"

        result = connectToMySQL("authors_books").query_db(query)

        return result
    

    @classmethod
    def books_with_no_likes(cls,data:dict):

        query="""
        SELECT * FROM books
        WHERE books.id NOT IN(
            SELECT book_id FROM authors_books 
            WHERE author_id = %(id)s
        )
        """

        result = connectToMySQL("authors_books").query_db(query,data)
        print(result)

        no_liked_books: list = []

        for book in result:
            no_liked_books.append(cls(book))

        print(no_liked_books)
        return no_liked_books
    
    @classmethod
    def add_author_to_favorite(cls,data: dict):

        query = """INSERT INTO authors_books(author_id, book_id)
        VALUES ( %(author_id)s, %(book_id)s )"""

        return connectToMySQL("authors_books").query_db(query,data)
    

    @classmethod
    def get_book(cls, data):

        query = """SELECT * FROM books
        LEFT JOIN authors_books ON books.id = authors_books.book_id
        LEFT JOIN authors ON authors.id = authors_books.author_id
        WHERE books.id = %(id)s;"""

        response = connectToMySQL("authors_books").query_db(query, data)

        book = cls(response[0])

        
        for row in response:
            if row["book_id"] is not None:
                
                print(row)
                author_data={
                    "id":row["author_id"],
                    "name":row["name"],
                    "created_at":row["authors.created_at"],
                    "updated_at":row["authors.updated_at"]
                }
                book.favorite_authors.append(authors.Author(author_data))

        print(book)
        return book