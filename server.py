from flask import Flask, render_template, redirect, request
from book import Book
from author import Author
from favorite import Favorite

app = Flask(__name__)
@app.route('/authors')
def home():
    authors = Author.get_all_authors()
    return render_template('/authors.html', authors = authors)

@app.route('/books')
def books():
    books = Book.get_all_books()
    return render_template('/books.html', books = books)

@app.route('/authors/new', methods=['POST'])
def newAuthor():
    new_author={
        'name': request.form['name']      
    }
    Author.createAuthor(new_author)
    return redirect('/authors')

@app.route('/authors/<int:id>')
def displayAuthor(id):
    # title of the book, book favorited by authors, and all authors that liked book
    data={
        'author_name': Author.getAuthorName(id),
        'booksFavoritedByAuthors': Favorite.getBooksFavoritedByAuthors(id),
        'books': Book.get_all_books(),
        'id': id
    }
    return render_template('author.html', data=data)

@app.route('/books/<int:id>')
def bookInfo(id):
    # title of the book, book favorited by authors, and all authors that liked book
    data={
        'title': Book.getTitle(id),
        'booksFavoritedByAuthors': Book.getBooksFavoritedByAuthors(id),
        'authors': Author.get_all_authors(),
        'id': id
    }
    return render_template('/book.html', data=data)


@app.route('/books/new', methods=['POST'])
def newBook():
    new_book = {
        'title': request.form['title'],
        'num_of_pages': request.form['num_of_pages']
    }
    Book.createBook(new_book)
    return redirect('/books')

@app.route('/books/<int:book_id>/favorite/new', methods=['POST'])
def favoriteBooks(book_id):
    Favorite.addFavoritedBook(book_id, request.form['author_id'])
    return redirect(f'/books/{book_id}')

@app.route('/authors/<int:author_id>/favorite/new', methods=['POST'])
def favoriteAuthor(author_id):
    Book.getBooksFavoritedByAuthors(id)
    Favorite.addFavoritedBook(request.form['book_id'], author_id )
    return redirect(f'/authors/{author_id}')


if __name__ == "__main__":
    app.run(debug=True)