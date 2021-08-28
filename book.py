# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Book:
    def __init__( self , data ):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all_books(cls):
        query = "SELECT * FROM books;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('books_schema').query_db(query)
        # Create an empty list to append our instances of friends
        books = []
        # Iterate over the db results and create instances of friends with cls.
        for book in results:
            books.append( cls(book) )
        return books

    @classmethod
    def createBook(cls, book):
        query= 'INSERT INTO books (title, num_of_pages, created_at, updated_at) VALUES (%(name)s,%(num_of_pages)s, NOW(), NOW());'
        data={
            'name':book['title'],
            'num_of_pages': book['num_of_pages']
        }
        connectToMySQL('books_schema').query_db(query, data)

    @classmethod
    def getTitle(cls, id):
        query='SELECT books.title from books where id = %(id)s;'
        data={
            'id': id
        }
        return connectToMySQL('books_schema').query_db(query, data)[0]["title"]

    @classmethod
    def getBooksFavoritedByAuthors(cls, id):
        query= 'SELECT authors.name FROM authors JOIN favorites ON favorites.author_id = authors.id AND favorites.book_id = %(id)s;'
        data={
            'id': id
        }
        return connectToMySQL('books_schema').query_db(query, data)
