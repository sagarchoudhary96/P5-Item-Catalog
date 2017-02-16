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

if __name__ == '__main__':
    app.debug = True
    app.run(host='', port = 5000)
