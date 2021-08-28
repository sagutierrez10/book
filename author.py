# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database
class Author:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # Now we use class methods to query our database
    @classmethod
    def get_all_authors(cls):
        query = "SELECT * FROM authors;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('books_schema').query_db(query)
        # Create an empty list to append our instances of friends
        authors = []
        # Iterate over the db results and create instances of friends with cls.
        for author in results:
            authors.append( cls(author) )
        return authors

    @classmethod
    def createAuthor(cls, author):
        query = 'INSERT INTO authors (name, created_at, updated_at) VALUES(%(name)s, NOW(),NOW());'
        data = {
            'name':author['name']
        }
        connectToMySQL('books_schema').query_db(query, data)

    @classmethod
    def getAuthorName(cls, id):
        query='SELECT authors.name from authors where id = %(id)s;'
        data={
            'id': id
        }
        return connectToMySQL('books_schema').query_db(query, data)[0]["name"]