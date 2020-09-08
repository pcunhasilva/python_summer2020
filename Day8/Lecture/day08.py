# Python - 2020 Summer Course
# Day 8
# Topic: Complexity, Recursion, and Sorting
# Instructor: Patrick Cunha Silva
# Former Instructors: Ryden Buttler, Erin Rossiter
#                     Michele Torres, David Carlson, and
#                     Betul Demirkaya
# First Instructor: Matt Dickenson


#---------- Recursion ----------#

# Function calls itself
# You need to know
#   - the base case
#   - when to call the function
#   - when to stop
# The typical example is n!
# A physical world example would be to place two parallel mirrors
#   facing each other. Any object in between them would be reflected 
#   recursively. 
# Make the code look clean
# Sequence generation is easier
# Logic behind is hard to follow sometimes
# Recursiveness are expensive and inefficient uses a lot of memory
# Hard to debug
# Source: https://www.programiz.com/python-programming/recursion

# Example, Factorial:
# n! = n * (n-1) * (n - 2) * ... * 2 * 1

# def nFactorial(n):
#   if base case:
#       return something
#   else:
#       return a recursive call

def nFactorial(n):
    if n == 1:
        return n
    else: 
        return n * nFactorial(n-1)
nFactorial(5)
# Using factorial from math
math.factorial(5)

#---------- Search Algorithms ----------#
import random

# 1 - Linear Search:
# returns element in a list and its position
def linear_search(mylist, element):
    steps = 0
    for item in mylist:
        steps += 1
        if item == element:
            print(steps)
            return item
    print(steps)
    return None

mylist = list(range(26))
random.shuffle(mylist)

linear_search(mylist, 1)
linear_search(mylist, 5)
linear_search(mylist, 10)

# 2 - Binary Search:
# returns element if it is in sorted list
def binary_search(sorted_list, element):
    print("Input list is {0}".format(sorted_list))
    print("Input size is {0}".format(len(sorted_list)))
    middle = len(sorted_list)//2
    median = sorted_list[middle]
    if len(sorted_list) <= 1:
        if element == median:
            return median
        else:
            return None
    if element < median:
        left = sorted_list[0:middle]
        return binary_search(sorted_list = left, element = element)
    else: 
        right = sorted_list[middle:]
        return binary_search(sorted_list = right, element = element)

mylist = range(0, 1000, 2)
binary_search(mylist, 72)
binary_search(mylist, 71)


#---------- Fibonacci Sequence ----------#

# Find n'th number in fibonacci sequence
def fib(n):
    if n<=1:
        return n
    return fib(n-1) + fib(n-2)

# fib(8) = fib(7) + fib(6) = 21
# fib(7) = fib(6) + fib(5) = 13
# fib(6) = fib(5) + fib(4) = 8
# fib(5) = fib(4) + fib(3) = 5
# fib(4) = fib(3) + fib(2) = 3
# fib(3) = fib(2) + fib(1) = 2
# fib(2) = fib(1) + fib(0) = 1
# fib(1) = 1
# fib(0) = 0 

for i in range(9):
    print("{0} : {1}".format(i, fib(i)))


#---------- Sorting ----------#

my_numbers = [1, 9, 8, 5, 4, 6, 0, 2, 3, 7]

# Selection Sort
# 1) Find minimum of the unsorted list
# 2) Remove minimum and place it in first element on new list
# 3) Repeat until unsorted list is empty

def selection_sort(numbers):
    # Answer object 
    numbers = numbers.copy()  
    answer = []
    while len(numbers) > 0:
        answer.append(min(numbers))
        del numbers[numbers.index(answer[-1])]    
    return answer

selection_sort(numbers = my_numbers)


# Bubble Sort
# 1) Compare first two contiguous elements, swap if necessary
# 2) Compare next two contiguous elements, swap if necessary
# 3) Continue until end of list
# 4) If swaps occurred in 1 - 3, repeat for first n - 1 elements
# Ex: https://www.geeksforgeeks.org/bubble-sort/

def bubble_sort(numbers): # Not the most efficient
    # Answer object 
    answer = numbers.copy()
    # N of numbers in numbers
    n = len(numbers) - 2
    # Index used in the while loop
    i = 0
    # Swap indicator
    swap = True
    # Object to stop the while loop
    notSwap = len(my_numbers) - 2
    while notSwap != 0:   
        if answer[i] > answer[i + 1]: # Compare numbers
            answer[i], answer[i + 1] = answer[i + 1], answer[i] # Swap numbers
            if i == n: # Check index
                i = 0
            else: 
                i += 1            
        else:
            if i == n: # Check index
                i = 0
                notSwap = n
            else: 
                notSwap -= 1
                i += 1
    return answer
                   
bubble_sort(my_numbers)

# Bogo Sort
# 1) Randomize number order
# 2) If sorted: stop; else: repeat

import random 

def bogo_sort(numbers):
    answer = numbers.copy() 
    while answer != sorted(numbers):
      random.shuffle(answer) 
    return answer

bogo_sort(my_numbers)


# Insertion Sort
# 1) Start with the element in the second position
# 2) Insert it to the correct position to the left
# - Check left-most element until value is greater
# 3) Continue to next position
# Ex: https://www.geeksforgeeks.org/insertion-sort/
 


#---------- Complexity ----------#

# The amount of time/the number of operations need to complete a task.
# O(n) notation:
#   - Big-O notation is a relative representation of the complexity of 
#     an algorithm.
#   - Classify algorithms according to how their running time 
#     or space requirements grow as the input size
#   - Informally, we can think of the Big-O notation as 
#     the run time in the worst case scenario 


# Table of common time complexities:

#       Name        Time Complexity

#   Constant Time         O(1)
# Logarithmic Time      O(log n)
#    Linear Time          O(n)
# Quasilinear Time     O(n log n)
#  Quadratic Time        O(n^2)
# Exponential Time       O(2^n)
#  Factorial Time         O(n!) 


# Examples:
# O(1) - Constant Time:
def o_1(x):
    out = x[0] + 1 
    return out

# O(n) - Linear Time:
def o_n(x):
    for i in range(x):
        x[i] += 1 
        return x

# O(n^2) - Quadratic Time:
def o_nsqr(x): 
    out = []
    for i in range(x): 
        for j in range(x):
          out.append(i + j) 
    return out

# O(2^n) - Exponential Time:
def fib(x): 
  if x <= 1: 
      return x
  return fib(x - 1) + fib(x - 2)


# Graphically
import matplotlib.pyplot as plt
import math
import numpy as np
import array

n = list(range(1, 11))
O1 = [1 for i in n]
OLogN = [math.log(i) for i in n]
OnLogN = [i * math.log(i) for i in n]
On2 = [i * 2 for i in n]
O2n = [2 ** i for i in n]
OnF = [math.factorial(i) for i in n]

plt.plot(n, O1, 'r-', label = "O(1)")
plt.plot(n, OLogN, 'b-', label = "O(Log n)")
plt.plot(n, OnLogN, 'g-', label = "O(n Log n )")
plt.plot(n, On2, 'y-', label = "O(2n)")
plt.plot(n, O2n, 'p-', label = "O(n^2)")
plt.plot(n, OnF, 'k-', label = "O(n!)")
plt.xlim(1, 10)
plt.ylim(1, 100)
plt.xlabel('N')
plt.ylabel('Big O')
plt.legend()
plt.show()

# See Towards Data Science for more 
# information on the Big O notation:
# https://bit.ly/3iYs4kb 



#---------- Plotting ----------#

#pip install matplotlib

import matplotlib.pyplot as plt

# x-axis: # of elements in list
x1 = range(1, 101) 
x2 = range(1, 101) 
# y-axis: time
y1 = range(1, 101) 
y2 = [i * 0.5 for i in range(1, 101)]
# adjust the area around the plot
plt.subplots_adjust(left = .13, right = .95, top = .9, bottom = .3) 
# Plot the data
plt.plot(x1, y1)
plt.plot(x2, y2)
# Add a legend
plt.legend(['hi', 'bye'], loc = "upper left", prop = {"size":10})
# y label
plt.ylabel("Y")
# x label
plt.xlabel("X")
# plot title
plt.title("The Effect of Different Sort Algorithms on Runtime")
# plot description
txt = """
Maybe a description here
"""
plt.figtext(.5, .05, txt, fontsize = 10, ha = "center")
# Display plot, use the option block=False
# otherwise you will need to close the plot manually
plt.show(block=False)
# Save plot
plt.savefig('plot.pdf')
# Close plot
plt.close()



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