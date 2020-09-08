# Python - 2020 Summer Course
# Day 8
# Topic: More on SQL and Database (Jin's question on True/False)
# Instructor: Patrick Cunha Silva
# Former Instructors: Ryden Buttler, Erin Rossiter
#                     Michele Torres, David Carlson, and
#                     Betul Demirkaya
# First Instructor: Matt Dickenson
# This file was added to the course by Patrick Cunha Silva

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, and_, or_
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy import select

import os 
os.chdir('/Users/pcunhasilva/Desktop')
# Some info about sqlalchemy
print(sqlalchemy.__version__)

# Connect to the local database
engine = sqlalchemy.create_engine('sqlite:///books.db', echo=True)

# Declare Base
Base = declarative_base() 

# Define some schemas
class Book(Base):
    __tablename__ = 'books'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    main_character = Column(String)
    year = Column(Integer)
    
    ## how will this table speak to other tables?
    author_id = Column(Integer, ForeignKey('authors.id'))
    
    def __init__(self, name, main_character=None, year=None):
      self.name = name
      self.main_character = main_character
      self.year = year
      
    def __repr__(self):
      if self.author: 
        return "<Book(%s by %s)>" % (self.name, self.author.name)
      return "<Book(%s)>" %(self.name)



class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    ## what does this do?
    country_id = Column(Integer, ForeignKey('countries.id'))

    ## what does this do?
    books = relationship('Book', backref='author')

    def __init__(self, name):
      self.name = name
    
    def __repr__(self):
      return "<Author('%s')>" % (self.name)

class Country(Base):
    __tablename__ = 'countries'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    capital = Column(String)
    
    ## what does this do?
    authors = relationship('Author', backref='country')
      
    def __init__(self, name, capital=None):
      self.name = name
      self.capital = capital
    
    def __repr__(self):
      return "<Country('%s')>" % (self.name)

# First time create tables
Base.metadata.create_all(engine) 

# Check Country table
Country.__table__  
Book.__table__ 

# Create instances of Book, Author, and Country
book1=Book('war and peace')
author1=Author('tolstoy')
country1=Country('russia')

# Add author to book
book1.author=author1
# Add country to author
author1.country=country1

# Create a session to actually store things in the db
Session = sessionmaker(bind=engine)
session = Session()

# Add data
session.add(book1)
session.add(author1)
session.add(country1)

# Add two more books
book2=Book('anna karenina')
book2.author=author1
session.add(book2)
book3=Book('tale of two cities')
session.add(book3)

# change db
session.commit()

# Print Book and Author
for row in session.query(Book, Author):
    print(row)
# Wait, Dickens wrote tale of two cities. 
# The information from Author is recycled 

# This will give us the correct answer  
for b, a in session.query(Book, Book.author):
    print(b, a)
# Maybe not, what is happening?

# Let's add the book id
for b, a in session.query(Book, Book.author):
    print(b.id, b.name, a)
# Okay, we see that each element in b is being printed more than one.

# Let's check if there are duplicates in Book
for b in session.query(Book):
    print(b.id, b.name)    
# We don't have duplicates in Book. What is happening?

# Check schema of Book
Book.__table__
# There is no author attribute

# Count instance in Book, Book.author, and each attribute in Book
session.query(Book).count() # Book
session.query(Book.author).count() # Book.author
session.query(Book.author_id).count() # Book.author_id
session.query(Book.id).count() # Book.id
session.query(Book.main_character).count() # Book.main_character
session.query(Book.name).count() # Book.name
session.query(Book.year).count() # Book.year

# Get Book and Book.author
b = session.query(Book).all()
a = session.query(Book.author)

# Loop over b, then a
for i in b:
  print(i)

for i in a:
  print(i)

# Print Author.id
authors_ids = session.query(Author.id).all()
for i in authors_ids:
  print(i)

# Print Book.author_id
book_authors_ids = session.query(Book.author_id).all()
for i in book_authors_ids:
  print(i)

# Put everthing together
s = select([Author.id == Book.author_id])
result = session.execute(s)
for i in result:
  print (i)

# How can we avoid it?
# Print Book and Author
for row in session.query(Book, Book.author).filter(Author.id == Book.author_id):
    print(row)    

# Or we can use join with Author
for row in session.query(Book).join(Author):
    print(row)

# So, what does Query do?
# It combines the two tables. 
# If they don't have the same length, the shorter will be recycled

# Example:
for i, j in session.query(Book.name, Author.name):
     print(i, j)

# How to avoid it?
# 1) Join
for i, j in session.query(Book.name, Author.name).join(Author):
  print(i, j)

# 2) Filter
for i in session.query(Book.name, Author.name).filter(Book.author_id == Author.id):
  print(i)


