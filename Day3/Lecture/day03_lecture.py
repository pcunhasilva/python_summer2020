# Python - 2020 Summer Course
# Day 3
# Topic: Errors, Exceptions, and Testing
# Instructor: Patrick Cunha Silva
# Former Instructors: Ryden Buttler, Erin Rossiter
#                     Michele Torres, David Carlson, and
#                     Betul Demirkaya
# First Instructor: Matt Dickenson

#---------- Types of Errors ----------#


# 1- Syntax error
#   - Errors related to language structure.
#   - Forgotten symbols, types, or confusing object names. 
#   - Check the ˆ!
# A syntax error happens when Python can’t understand the command. 

# Example:
while True print 'Hello world'
# In [1]: while True print 'Hello world'                                          
#   File "<ipython-input-1-87563a47f7ef>", line 1
#     while True print 'Hello world'
#                    ^
# SyntaxError: invalid syntax

# 2 - Runtime error
#   - Errors during the execution of program.
#   - eg. TypeError, NameError, ZeroDivisionError
# A run-time error happens when Python understands and runs the command, 
# but cannot following the instructions.

# Example 1 (NameError):
callMe = "Maybe"
print(callme)
# NameError                                 Traceback (most recent call last)
# <ipython-input-5-943eac5ae18e> in <module>
# ----> 1 print(callme)
#
# NameError: name 'callme' is not defined

# Example 2 (TypeError):
print("you cannot add text and numbers" + 12)
# TypeError                                 Traceback (most recent call last)
# <ipython-input-6-134cd69869df> in <module>
# ----> 1 print("you cannot add text and numbers" + 12)

# TypeError: must be str, not int


# 3 - Semantic error
# - The program will run successfully but the output is not what you expect.
# Example:
def avg(x, y):
    return x + y / 2
myAvg = avg(2, 2) 
print(myAvg)

# Very common, very annoying and, unfortunately, without indication that they exist.


#---------- Debugging Tips ----------#

# 1 - Do not use reserved/keywords:
# - You can check the reserved/keywords using:
import keyword
keyword.kwlist
# 2 - A colon is included after for, while, if, else, def, class, etc.
def avg(x, y): return (x + y)/2
avg(2, 2)
# 3 - Parentheses and quotations are closed properly.
print((10*2) + (5*3))
# 4 - Use = and == correctly
myAvg = avg(2, 2)
2 == myAvg
# 5 - Use correct indentation
x = 1
while x < 5:
    x += 1
    print(x)
# 6 - Indexing begins at 0
for i in range(0, 5):
    print(i)

#---------- Exceptions ----------#

# We use them when we expect error to occur, very useful when web scraping
# We define what to execute when there is an error
# We should deal with multiple errors separately

# List of exceptions:
#  - raise: 
#       to create exceptions or errors
#  - pass 
#       to continue execution without doing anything
#  - try: 
#       tries executing the following
#  - except TypeError: 
#       runs if a Type Error was raised
#  - except: 
#       runs for all types of errors or exceptions
#  - else:  
#       runs if there was no exception/error
#  - finally: 
#       always runs

# We can create our own exceptions using classes.

# Example 1, using raise Exception:

def exception_func(x):
    if x == 0:
        raise Exception("Cannot divide by 0") 
    else:
        return 5.0//x
print(exception_func(1))
print(exception_func(0))

# Example 2, using built-in exceptions (ZeroDivisionError)
def exception_func(x):
    try:
        ans = 5.0//x
    except ZeroDivisionError:
        ans = "Cannot divide by 0"
    finally:
        return ans 
print(exception_func(1))
print(exception_func(0))

# Here is a list with (most) of the exceptions in Python:
# https://airbrake.io/blog/python-exception-handling/class-hierarchy

# Example 3, try and exception
try:
    "hi" // 12 ## type error
    5//0 ## zero division error
    print(var//12) ## name error
except:
    print("caught an exception")
# We use this format when we don't know what is causing the issue.

# Example 4, a more complex example
def divide_two_things(thing1, thing2):
    try:
        out = float(thing1) // thing2
    except TypeError:
        print("Make sure you have two numbers, returning None.")
        out = None
    except ZeroDivisionError:
        print("Can't divide by 0, returning None.")
        out = None
    except:
        print("I caught an unexpected error! Returning None.")
        out = None
    else:
        out = thing1 // thing2
    finally:
        return out

divide_two_things("hi", 12)
divide_two_things(12, 0)
divide_two_things(5, 5)

## Doesn't catch semantic errors, though!
divide_two_things(10, 3) 

# Exceptions are helpful so our code doesn't break!
# Example 5:
list1 = [15, 9, 8] 
list2 = [1, 1, 0]
# zip() creates an iterator of tuples based on iterable objects (such as lists)
[print("i value = {} and j value {}".format(i, j)) for i, j in zip(list1, list2)]
# We can loop over the two lists using divide_two_things()
newlist = [divide_two_things(i,j) for i, j in zip(list1, list2)]
newlist

# Short Class Activity
# Let's say we don't care about floats... rounding down is cool.
# What type of error would occur? 
# How can we fix it?
def print_integer(integer):
    try:
        integer / 1
    if TypeError:
        pass
    else:
        return "Here is my integer: " + str(integer)
    
print_integer(2)
print_integer('22')
print_integer('banana')

# We can nest if and else within try and exception
def print_integer(integer):
    try:
        ## if a whole number
        if integer % 1 == 0:
            return "Here is my integer: " + str(integer)
        else:
            return "This number has decimals!"
    except:
        raise TypeError("Enter a number!")

print_integer('22')
print_integer(1.2)
print_integer(1)  


# We can create your own exception      
class CustomException(Exception): 
  def __init__(self, value):
    self.value = value
  def __str__(self):
    return str(self.value)

# use
raise CustomException(3)

# Our custom exception is the integer cannot be 10, 20, or 30.
# Since this is a ValueError unique to our situation, 
# we need to catch it ourselves.
def print_integer(integer):
    bad_numbers = [10, 20, 30]
    try:
        if integer in bad_numbers:
            ## raise it ourselves
            raise CustomException(integer)
        if integer % 1 == 0:
            print("Congratulations! You entered an integer!")
    ## then catch it
    except CustomException as e:
        ## and print our message
        raise ValueError("Your number cannot be: %d" % e.value)
        return None
    except TypeError:
        print("You didn't enter a number.")
        return None
    else:
        return integer
print_integer(10) # Let check the output


# Short Class Activity, how can we fix it?
mylist = [1, 2, 3, 4.5, "6", "7.8", 8, 9, "done"]
out = [mylist.pop(0)]
for i in mylist:
    try:
        out.append(out[-1] + i)
    except TypeError:
        print('It is not a number')

# Answer:
mylist = [1, 2, 3, 4.5, "6", "7.8", 8, 9, "done"]
out = [mylist.pop(0)]
for i in mylist:
    try:
        out.append(out[-1] + i)    
    except TypeError:
        print('Not a float or int.')
out



#---------- break, continue, and else ----------#

# These statements can be handy using while or for loops.
# - break 
#   stops the loop
# - continue 
#   moves on to the next iteration
# - else 
#   executed only if all iterations are completed

for n in range(2, 10):
    for x in range(2, 5): 
        if 5 % x == 0:
            print(5, 'equals', x, '*', 5//x)
            break
    else:
        print(5, 'is a prime number')

# We want to only print "n is a prime number" once
# We want to avoid repetition if 2x3 = 6, 
# we don't need to print 3x2 = 6
# How we solve it?


# Solution:
for n in range(2, 10):
    for x in range(2, n): 
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
    else:
        print(n, 'is a prime number')

# See lecture 1 for more on pass, break, and continue 

#---------- Unit Test ----------#

# Write tests before / alongside your code
# Tests the smallest possible unit of your code 
# Forces code structure
# Allows easier integration of multiple functions
# Much easier to return to code:
#    Write a test for what you want to implement next.
# Easier to make code changes
# We can easily incorporate lots of these into our work flow.
# Test-driven development

# We can use assert to test our code within our script
assert sum([1, 2, 3]) == 6 # It will not return anything if it is correct
assert sum([2, 3]) == 6
assert avg(2, 2) == 2
assert avg(2, 2) == 4

# We can also use a test runner, such as unittest


import unittest # unit testing module 
from myscript import * # the script you want to test

# Mock example
class Mytest(unittest.TestCase): 

    def test_one(self):
        self.assertEqual("result", script.func(input))

    def test_two(self):
        thing1 = script.func(input1)
        thing2 = script.func(input2) 
        self.assertNotEqual(thing1 , thing2)
    
    # if you want to run the test with this script
    if __name__ == '__main__': 
        unittest.main()

# Example
# Open file mytest.py



# Functions to test 
# Method                      Checks that
# assertEqual(a, b)           a == b
# assertNotEqual(a, b)        a != b
# assertTrue(x)               bool(x) is True
# assertFalse(x)              bool(x) is False
# assertIs(a, b)              a is b
# assertIsNot(a, b)           a is not b
# assertIsNone(x)             x is None
# assertIsNotNone(x)          x is not None
# assertIn(a, b)              a in b
# assertNotIn(a, b)           a not in b
# assertIsInstance(a, b)      isinstance(a, b)
# assertNotIsInstance(a, b)   not isinstance(a, b)



# We need the keyword "with" when using self.assertRaises():
    with self.assertRaises(Exception):
        outfunction()
# "with" is a keyword to use a context manager 
# See: https://www.geeksforgeeks.org/context-manager-in-python/

# More about unittest at: https://docs.python.org/3/library/unittest.html


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
