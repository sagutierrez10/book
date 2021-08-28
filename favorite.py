# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Favorite:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all_favorites(cls):
        query = "SELECT * FROM favorittes;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('books_schema').query_db(query)
        # Create an empty list to append our instances of friends
        favorites = []
        # Iterate over the db results and create instances of friends with cls.
        for favorite in results:
            favoritess.append( cls(favorite) )
        return favorites

    @classmethod
    def addFavoritedBook(cls,book_id, author_id): 
        query= 'INSERT INTO favorites (author_id, book_id) VALUES (%(author_id)s,%(book_id)s);'
        data={
            'author_id': author_id,
            'book_id': book_id
        }
        connectToMySQL('books_schema').query_db(query, data)

    @classmethod
    def getBooksFavoritedByAuthors(cls, author_id):
        query= 'SELECT books.title, books.num_of_pages FROM books JOIN favorites ON books.id = favorites.book_id AND favorites.author_id = %(id)s;'
        data={
            'id': author_id
        }
        return connectToMySQL('books_schema').query_db(query, data)