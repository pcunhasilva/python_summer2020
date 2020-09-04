# Python - 2020 Summer Course
# Day 2
# Topic: Namespace and classes
# Instructor: Patrick Cunha Silva
# Former Instructors: Ryden Buttler, Erin Rossiter
#                     Michele Torres, David Carlson, and
#                     Betul Demirkaya
# First Instructor: Matt Dickenson

#---------- Namespace and Scope ----------#

# Namespace: a naming system for making names unique to avoid ambiguity.
#            It maps names to objects.
# Scope: level at which ``a namespace is directly accessible'' 
#        It is the area of a program where a name can be unambiguously used.
# Python follows the hierarchy:
#  - Innermost scope: local names
#  - Scope of enclosing functions, innermost first
#  - Next-to-last scope: global names in current module
#  - Outermost scope: built-in names such as int(), sum() ()


# A silly function that prints an integer
def print_int(int): 
    int = 5
    print('Here is an integer: %s' % int) 

print_int('int') # What’s wrong with this?

# The function searches within itself (local scope) then the global scope.

# Let's redefine the function print_int()
def print_int(): 
    print('Here is an integer: %s' % int)
print_int() # What is going to happen?

# Now, the function works because it int is a build-in name.
# Do not use build-in or module names to name objects!

# Let's try a new function for the product of random uniform draws
def random_product(lower, upper): 
    random1
    random2
    return random1 * random2
random_product(0, 1) # What is happening?

# But, it would have (wrongly) worked if we had random1 and random2 defined in our global space
random1 = 2
random2 = 2
random_product(0, 1)

# We must define values for objects random1, random2 
# To do so, we must load module for random sampling

import random
def random_product(lower, upper): 
    random1 = uniform(lower, upper)
    random2 = uniform(lower, upper)
    return random1 * random2
print(random_product(0, 1)) # Wait, random is not defined!

# We have two options now. We may add the module name before global name
def random_product(lower, upper): 
    random1 = random.uniform(lower, upper)
    random2 = random.uniform(lower, upper)
    return random1 * random2
print(random_product(0, 1))

# This is equivalent to use package_name::function_name() in R.

# Or we can import the method as a global name.
from random import uniform 
def random_product(lower, upper): 
    random1 = uniform(lower, upper)
    random2 = uniform(lower, upper)
    return random1 * random2
print(random_product(0, 1))

# We can also import all methods from a module using * after import
from random import * 



#---------- Classes ----------#

# Classes help you create objects with 
#  - certain attributes
#  - ability to perform certain functions.
# An instance is a particular realization of a class.
# We use attributes and methods of classes all the time in R.

# create a class
class Human:
    # attribute for the class
    latin_name = 'homo sapien'
# create an instance of a class and name it ’me.’ 
me = Human()

# Check type
type(me)
# Check methods and attributes
dir(me)

# All instances share the same attributes
you = Human()
me.latin_name
you.latin_name
you.latin_name == me.latin_name


# We can define an initialization method (__int__) for our class
# create a class
class Human:
    # attribute for the class
    latin_name = 'homo sapien'
    # add attributes for the instance
    # this is an initializer (or constructor) 
    def __init__(self, age, pronoun, name):
        self.age = age 
        self.pronoun = pronoun
        self.name = name 

me = Human() # Now we need to add age and name
me = Human(age = 32, pronoun = 'he', name = 'Patrick')
# We can check all the attributes for the instance
dir(me)

# We may include default arguments to the initializer, as we do with methods
class Human:
    # attribute for the class
    latin_name = 'homo sapien'
    # add attributes for the instance
    # this is an initializer ()or constructor) 
    def __init__(self, age, pronoun = 'None', name = 'None'):
        self.age = age 
        self.pronoun = pronoun
        self.name = name 
me = Human(age = 32)
# Make sure you set the non-default arguments first in our new class.
me.age
me.pronoun
me.name

# When using classes, we can define methods that are specific for that class
class Human:
    # attribute for the class
    latin_name = 'homo sapien'
    # add attributes for the instance
    def __init__(self, age, pronoun, name = 'None'): 
        self.age = age
        self.pronoun = pronoun
        self.name = name
    # add functions for the class
    def speak(self, words): 
        return words
    def introduce(self):
        if self.pronoun in ['she', 'She']: 
            return self.speak("Hello. I'm Ms. %s" % self.name)
        elif self.pronoun in ['he', 'He']: 
            return self.speak("Hello. I'm Mr. %s" % self.name)
        else: 
            return self.speak("Hello. I'm %s" % self.name)        

# We can create an instance of Human, then use the methods associated with it.
me = Human(age = 32, pronoun = 'he', name = 'Patrick')
me.speak('Hi!')
me.introduce()

#---------- Inheritance and Polymorphism ----------#

# Inheritance enables you to create sub-classes that inherit the methods of another class.

class PhDStudent(Human):
    pass

me = PhDStudent(age = 32, name = 'Patrick', pronoun = 'he')
me.speak("Hi, I'm a political science PhD student.")

# We can add more attributes to our new class
class PhDStudent(Human):
    def __init__(self, age, pronoun, name, field):
        Human.__init__(self, age, pronoun, name)
        self.field = field
me = PhDStudent(age = 32, name = 'Patrick', pronoun = 'he', field = 'Comparative politics')
me.field

# Polymorphism adapts a given method of a class to its sub-classes.
# Same function name being uses for different types (classes)

# In-built example (from https://www.geeksforgeeks.org/polymorphism-in-python/):
# len() being used for a string
print(len('patrick'))
# len() being used for a list
print(len([10, 20, 30]))

# With user-created classes:
class AP:
    def discipline(self):
        print("American Politics is Political Science's subfield")

class CP:
    def discipline(self):
        print("Comparative Politics is Political Science's subfield")

class IR:
    def discipline(self):
        print("International Relations is Political Science's subfield")

obj_cp = CP()
obj_ap = AP()
obj_ir = IR()
for sub in (obj_cp, obj_ir, obj_ap):
    sub.discipline()


#---------- A more complicated example ----------#

# - Add a student's name to the roster for a grade
# - Get a list of all students enrolled in a grade
# - Get a sorted list of all students in all grades.
# 
# Note that all our students only have one name.

class School():
    def __init__(self, school_name): #initialize instance of class School with parameter name
        self.school_name = school_name #user must put name, no default
        self.db = {} #initialize empty dictionary to store kids and grades
        
    def add(self, name, student_grade): #add a kid to a grade in a given instance of School
        if student_grade in self.db: #check if the key for the grade already exists
            self.db[student_grade].append(name) #add kid to the dictionary
        else: self.db[student_grade] = [name] #if the key doesn't exist, create it and kid starts a new list 

    def sort(self): #sorts kids alphabetically and returns them in tuples (because they are immutable)
        sorted_students={} #sets up an empty dictionary to store sorted tuples
        for key in self.db.keys(): #loop through each key, automatically ordered
            sorted_students[key] = tuple(sorted(self.db[key])) #add dictionary entry with key = grade and entry = tuple of kids
        return sorted_students

 
    def grade(self, check_grade):
        if check_grade not in self.db: return None #if the key doesn't exist, there are no kids with that grade: return None
        return self.db[check_grade] #return elements within dictionary (kids with the specific grade)

    def __str__(self): #print method will display the school name and sorted kids
        return "%s\n%s" %(self.school_name, self.sort())


# Create an instance of School 
washu = School("Washington University in St. Louis")

# Add Students using .add method
washu.add("Patrick", 2)
washu.add("Nick", 2)
washu.add("Luwei", 2)
washu.add("William", 5)

# Print the dictionary
washu.db

# We can sort the students within grade
sorted_students = washu.sort()
print(sorted_students)
washu.db

# Note that our print method already sorts the students
print(washu)

# Search students using their grades
print(washu.grade(4))
print(washu.grade(2))

# Can we add a different sort method to sort the students ~within~ the object?

# We can use the method below to solve it
def sort(self): #sorts kids alphabetically and returns them in tuples (because they are immutable)
    sorted_students={} #sets up empty dictionary to store sorted list
    for key in self.db.keys(): #loop through each key, automatically ordered
        sorted_students[key] = list(sorted(self.db[key])) #add dictionary entry = grade and entry = list of kids
    self.db = sorted_students # Update self
    return sorted_students   



#---------- Inheritances Another Example  ----------#

class Parent():
  def __init__(self, sex, firstname, lastname):
    self.sex = sex
    self.firstname = firstname
    self.lastname = lastname
    self.kids = [] ## Child objects

  def role(self):
    if self.sex == "Male":
      return "Father"
    else:
      return "Mother"

  def have_child(self, name):
    child = Child(name, self)
    print(self.firstname + " is having a child named " + child.name())
    print("They will make a very good " + self.role())
    self.kids.append(child)
    return child

  def list_children(self):
    for kid in self.kids:
      print("I am the " + self.role() + " of " + kid.name())


class Child():
  def __init__(self, firstname, parent):
    self.parent = parent 
    self.lastname = parent.lastname
    self.firstname = firstname

  def set_name(self, new_first_name, new_last_name):
    self.firstname = new_first_name
    self.lastname = new_last_name

  def name(self):
    return "%s %s" % (self.firstname, self.lastname)

  def introduce(self):
    return "Hi I'm " + self.name()

  def siblings(self):
    for kid in self.parent.kids:
      if kid != self:
        print("I have a sibling named " + kid.name())
        

# Create mom, an instance of Parent
mom = Parent("Female", "Jane", "Smith")
# Add a Child (jill) to mom
jill = mom.have_child("Jill")
# Rename the child
jill.set_name("Jillian", "Jones")
print(jill.introduce())
mom.list_children()

# Check if jill is daughter of Jane
print(jill == mom.kids[0])

# Add another Child (jack) to mom
jack = mom.have_child("Jack")
print(jack.introduce())

# Print the list of children from Jane
jack.parent.kids[0].parent.list_children()
mom.list_children()

# Print jack's siblings
jack.siblings()



#---------- Inheritance and Polymorphism Another Example  ----------#
# Remember:
# Inheritance -- child gets all method of the parent class(es)
# Polymorphism -- child methods can override parent methods of same name


# "parent" or general class
class Animal:
    
    living = "Yes!" ## attribute of all Animal objects

    def __init__(self, name): # Constructor of the class
        self.name = name
      
    def talk(self): # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")
    # An abstract method is a method that is declared, but contains no implementation.

    def furry(self): ## function object of all Animals
        return True


# "children" or specific classes
class Cat(Animal):
    def talk(self):
        return self.meow() 
    def meow(self):
        return 'Meow!'

class Dog(Animal):
    def talk(self):
        return self.bark()
    def bark(self):
        return 'Woof! Woof!'

class Fish(Animal):  
    def bubbles(self):
        return 'blubblub'
    def furry(self):
        return False

# Create a cat
leonard = Cat("Leo")
# Now, a dog
gus = Dog("Gus")
# Lastly, a fish
nemo = Fish("Nemo")

# Create a list with all animals
animals = [leonard, gus, nemo]

# Why did this happen?  How do we fix it?
for animal in animals:
    print(animal.name + ': ' + animal.talk())

# We would need to modify class Fish

## What happened here?
for animal in animals:
    print(animal.name + ': ' + str(animal.furry()))


# Copyright of the original version:

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
