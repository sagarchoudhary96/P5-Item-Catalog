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
@app.route('/book/new', methods=['GET', 'POST'])
def newBook():
    if request.method == 'POST':
        bookName = request.form['bookName']
        bookAuthor = request.form['authorName']
        coverUrl = request.form['bookImage']
        description = request.form['bookDescription']
        bookCategory = request.form['category']
        newBook = BookDB(bookName = bookName, authorName = bookAuthor, coverUrl = coverUrl, description = description, category = bookCategory)

        session.add(newBook)
        session.commit()
        return redirect(url_for('showBooks'))
    else:
        return render_template("newItem.html", currentPage = "new")

# for showing book of different category
@app.route('/books/category/<string:category>')
def sortBooks(category):
    books = session.query(BookDB).filter_by(category = category).all()
    return render_template("main.html", books = books, currentPage = 'main')


if __name__ == '__main__':
    app.debug = True
    app.run(host='', port = 5000)
