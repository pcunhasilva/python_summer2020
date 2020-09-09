# Python - 2020 Summer Course
# Day 8
# Topic: More on SQL and Database (Loading a Database)
# Instructor: Patrick Cunha Silva
# Former Instructors: Ryden Buttler, Erin Rossiter
#                     Michele Torres, David Carlson, and
#                     Betul Demirkaya
# This is an addition to the course made by Patrick Cunha Silva


from sqlalchemy import *
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, and_, or_
from sqlalchemy.orm import relationship, backref, sessionmaker
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
import os

# Set WD
os.chdir('/Users/pcunhasilva/Dropbox/PythonClass/Summer2020/Day7/Lab')

# The simplest usage is to reflect an existing database into a new model.
Base = automap_base()

# Create an engine
engine = sqlalchemy.create_engine('sqlite:///geog.db', echo=True)

# reflect the tables
Base.prepare(engine, reflect=True)

# Check the classes in our original db
dir(Base.classes)

# mapped classes that we have in our original database
Department = Base.classes.departments
Region = Base.classes.regions
Town = Base.classes.towns

# Create a session to store new things in the db
Session = sessionmaker(bind=engine)
session = Session()

# Create region 6
reg6 = Region(name = 'Region 6')

# Create departments, nested in regions
dept6 = Department(deptname = 'Department 6')
reg6.departments_collection.append(dept6)

# Create towns, nested in departments
t10 = Town(name = 'j', population = 750000)
dept6.towns_collection = [t10]

# Add to our database
session.add_all([reg6])
session.add_all([dept6])
session.add_all([t10])

session.commit()

# Some example querying 
for town in session.query(Town).order_by(Town.id):
  print(town.id, town.name, town.population)

# Display the total number of inhabitants
# per department
for depart in session.query(Department.deptname, func.sum(Town.population).label('total')).join(Town).group_by(Department.deptname):
  print('{}. Total Population: {}'.format(depart.deptname, depart.total))

# Close connection
session.close()
