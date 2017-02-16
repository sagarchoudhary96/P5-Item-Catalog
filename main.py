from flask import Flask, render_template, request, redirect, url_for, flash
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, BookDB, User
import random, string

engine = create_engine('sqlite:///BookCatalog.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()


# for main page
@app.route('/')
@app.route('/books/')
def showBooks():
    books = session.query(BookDB).all()
    return render_template('main.html', books = books, currentPage = 'main')

# for adding new book
@app.route('/book/new/', methods=['GET', 'POST'])
def newBook():
    if request.method == 'POST':
        bookName = request.form['bookName']
        bookAuthor = request.form['authorName']
        coverUrl = request.form['bookImage']
        description = request.form['bookDescription']
        description = description.replace('\n', '<br>')
        bookCategory = request.form['category']
        newBook = BookDB(bookName = bookName, authorName = bookAuthor, coverUrl = coverUrl, description = description, category = bookCategory)

        session.add(newBook)
        session.commit()
        return redirect(url_for('showBooks'))
    else:
        return render_template("newItem.html", currentPage = "new", title = "Add New Book")

# for showing book of different category
@app.route('/books/category/<string:category>/')
def sortBooks(category):
    books = session.query(BookDB).filter_by(category = category).all()
    return render_template("main.html", books = books, currentPage = 'main', error = 'Sorry! No Book in Database With This Genre :(')

# to show book detail
@app.route('/books/category/<string:category>/<int:bookId>/')
def bookDetail(category, bookId):
    book = session.query(BookDB).filter_by(id = bookId, category = category).first()
    if book:
        return render_template("itemDetail.html", book = book, currentPage ='detail', title = book.bookName)
    else:
        return render_template("main.html", currentPage = 'main', error = 'No Book Found with this Category and Book Id :(')


# to edit book detail
@app.route('/books/category/<string:category>/<int:bookId>/edit/', methods=['GET', 'POST'])
def editBookDetails(category, bookId):
    book = session.query(BookDB).filter_by(id = bookId, category = category).first()
    if request.method == 'POST':
            bookName = request.form['bookName']
            bookAuthor = request.form['authorName']
            coverUrl = request.form['bookImage']
            description = request.form['bookDescription']
            description = description.replace('\n', '<br>')
            bookCategory = request.form['category']
            if bookName:
                book.bookName = bookName
            if bookAuthor:
                book.authorName = bookAuthor
            if coverUrl:
                book.coverUrl = coverUrl
            if description:
                book.description = description
            if bookCategory:
                book.category = bookCategory

            session.add(book)
            session.commit()
            return redirect(url_for('showBooks'))
    elif book:
        book.description = book.description.replace('<br>', '\n')
        return render_template("editItem.html", currentPage = 'edit', title = "Edit Book Details", book = book)
    else:
        return render_template("main.html", currentPage = 'main', error = 'No Book Found with this Category and Book Id :(')


if __name__ == '__main__':
    app.debug = True
    app.run(host='', port = 5000)
