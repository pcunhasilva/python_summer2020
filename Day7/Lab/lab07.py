import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, and_, or_
from sqlalchemy.orm import relationship, backref, sessionmaker

engine = sqlalchemy.create_engine('sqlite:///geog.db', echo=False)

Base = declarative_base() 

# Schemas
class Region(Base):
  __tablename__ = 'regions'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  departments = relationship("Department", backref = "region")

  def __init__(self, name):
    self.name = name 

  def __repr__(self):
    return "<Region('%s')>" % self.id 



class Department(Base):
  __tablename__ = 'departments'

  id = Column(Integer, primary_key=True)
  deptname = Column(String)
  region_id = Column(Integer, ForeignKey('regions.id')) 
  towns = relationship("Town", backref = "department")

  def __init__(self, deptname):
    self.deptname = deptname 

  def __repr__(self):
    return "<Department('%s')>" % self.id 



class Town(Base):
  __tablename__ = 'towns'

  id = Column(Integer, primary_key=True)
  name = Column(String)
  population = Column(Integer)
  dept_id = Column(Integer, ForeignKey('departments.id'))

  def __init__(self, name, population):
    self.name = name 
    self.population = population

  def __repr__(self):
    return "<Town('%s')>" % (self.name)




#First time create tables
Base.metadata.create_all(engine) 

#Create a session to actually store things in the db
Session = sessionmaker(bind=engine)
session = Session()

# Create regions
reg1 = Region('Region 1')
reg2 = Region('Region 2')
reg3 = Region('Region 3')

# Create departments, nested in regions
dept1 = Department('Department 1')
reg1.departments.append(dept1)

dept2 = Department('Department 2')
reg1.departments.append(dept2)

dept3 = Department('Department 3')
reg3.departments.append(dept3)

dept4 = Department('Department 4')
reg2.departments.append(dept4)


# Create towns, nested in departments
t1 = Town("a", 10000)
t2 = Town("b", 20000)
dept1.towns = [t1, t2]

t3 = Town("c", 30000)
t4 = Town("d", 40000)
dept2.towns = [t3, t4]

t5 = Town("e", 50000)
t6 = Town("f", 60000)
dept3.towns = [t5, t6]

t7 = Town("g", 70000)
t8 = Town("h", 80000)
dept4.towns = [t7, t8]

session.add_all([reg1, reg2, reg3])
session.add_all([dept1, dept2, dept3, dept4])
session.add_all([t1, t2, t3, t4, t5, t6, t7, t8])


session.commit()

# Some example querying 
for town in session.query(Town).order_by(Town.id):
  print(town.id, town.name, town.population)


# TODO: 
# 1. Display, by department, the cities having
#    more than 50,000 inhabitants.
# 2. Display the total number of inhabitants
#    per department






# Copyright (c) 2014 Matt Dickenson
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.