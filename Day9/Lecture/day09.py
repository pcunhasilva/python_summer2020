# Python - 2020 Summer Course
# Day 9
# Topic: Data types and Tricks
# Instructor: Patrick Cunha Silva
# Former Instructors: Ryden Buttler, Erin Rossiter
#                     Michele Torres, David Carlson, and
#                     Betul Demirkaya
# First Instructor: Matt Dickenson

# Useful site: https://book.pythontips.com/en/latest/index.html

import os
os.chdir('/Users/pcunhasilva/Dropbox/PythonClass/Summer2020/Day9/Lecture')

#pip install pandas
#pip install numpy
import pandas as pd
import numpy as np

#---------- Pandas ----------#

# Series:
# - nX1 array. Similar to a vector in R.
# - Hold any tupe of data, (integer, string, float, etc.)

# Create a pd.Series:
x = pd.Series([10, 100, 12, 5])
# We index a Series as we do with lists
x[0]


# DataFrame:
# - nXk array. Similar to a data.frame in R.
# - now columns and rows

# Creating a pd.DataFrame:

# The input can be a dictionary
dt = {'A' : 1.2, 'B' : [10, 8, 3, 4, 8, 6], "C" : "hi"}
df1 = pd.DataFrame(dt)
df1 # print the dataframe
df1.dtypes # data types

# The input can also be a list of lists
l = [[1.2], [10, 8, 3, 4, 8, 6], ["hi"]]
# We need to list the columns' names.
df2 = pd.DataFrame(l, columns = ["A", "B", "C", "D", "E", "F"])

# Note how they are different 
# Our first DataFrame
df1 # 6x3
# Our Second DataFrame
df2 # 3x6

# We can check the data type
df2.dtypes 

# We can check the row indexes
df2.index 

# And rename rows
df2 = df2.rename(index = {0:"One", 1:"Two", 2:"Three"})
df2
df2.index 

# There are different ways to add more columns

# Using list
df1 # original data
df1['D'] = [0, 2, 4, 6, 8, 10]
df1

# Using assign
df1 = df1.assign(E = ["x", "x", "x", "x", "x", None])
df1

# Using insert (we insert the new column at a specific position)
df1.insert(3, "F", ["K", "K", "K", "K", "K", "K"])
df1

# Some helpful commands

# head() and tail() work as they work in R
df1.head() # default shows the first 5 rows
df1.head(2) 
df1.tail() # default shows the last 5 rows

# Check the dataframe column's indexes
df1.columns

# describe the dataframe, similar to summary in R
df1.describe()

# sort the dataframe (using a specific column)
df1.sort_values(by = "B")

# indexing a DataFrame
df1["A"] # column A
df1["A"][0] ## column then row
df1[0:4] ## first 4 rows
df1.loc[:,["C"]] # All rows from column "C"
df1.loc[0:2, ["C"]] # First three rows from column "C"
df1.iloc[0:2, 0:2] # First two rows and two colunms

# Difference between .loc and .iloc:
# .loc: gets rows (columns) using labels
# .iloc: gets rows (columns) using positions 

# Read and Save csv files
my_data = pd.read_csv('test_csvfields.csv')
my_data.head()
# Save Data
my_data.to_csv('test_csvfields2.csv')


#---------- Numpy ----------#

# Create an 3x1x1 array
a = np.array([1, 2, 3])
a

# Create an 3x2x1 array
a = np.array([(1, 2, 3), (1, 2, 3)])
a
# Arrays are faster than lists 

# We can do mathematical operations
# If two arrays have the same dimension 
print(a.ndim)
a * a
a / a
a + a
a - a

# We can use arrays to create a DataFrame
# Create a 6x4 Matrix with random numbers 
a = np.random.randn(6,4)
a
df_array = pd.DataFrame(a, columns = ["A", "B", "C", "D"])
df_array

# More on numpy here: https://www.edureka.co/blog/python-numpy-tutorial/



#---------- Tuples ----------#

# Remember, Tuples are immutable
my_tuple = (1,'b',3,'d',5,'b')
my_tuple[1] = {'b':2}

# Indexing Tuples
my_tuple[0] ## element at index  0
my_tuple.index('b') ## Gives the index of 'b' - only the first occurence!
my_tuple.count('b') ## Gives the number of times 'b' occurs


#---------- Lists ----------#

# Create a list from 0 to 9 squared
my_square_list=[]
for i in range(0,10):
	my_square_list.append(i**2)
my_square_list

# We can do in one line:
my_square_list = [i**2 for i in range(10)]
my_square_list

# We can also use map()
# map is like apply/sapply in R
# lambda creates an anonymous function, like function(x)
# In R, we would write:
# sapply(0:9, function(x) x^2)
# In Python, we write:
my_square_list = map(lambda x: x**2, range(0,10))
# we need to transform the output into a list or tupple
my_square_list = list(my_square_list) 
my_square_list

# another way
def sqr(x): 
	return x**2

my_square_list = map(sqr, range(0,10))
list(my_square_list)


# Or:
my_square_list = list(map(sqr, range(0,10)))
my_square_list

# zip combines elements of 2 lists with matching indexes 
# into an interable of tuples
my_list = range(0,10)
# An simple example:
for i, j in zip(my_list, my_square_list): print(i * j)

# We can combine with map:
zipped = zip(my_list, my_square_list, map(lambda x: my_square_list[x] * my_list[x], range(0, 10)))
zipped # We need to make it a list or a tuple
list(zipped)

# We can also unzip the object using "*"
zipped = zip(my_list, my_square_list, map(lambda x: my_square_list[x] * my_list[x], range(0, 10)))
unzipped = zip(*zipped)
unzipped
list(unzipped)

# filter
# returns elements only for which condition is True
x = filter(lambda x: x == 1, [1,2,3]) 
x
# we need to pass the output to list() or tuple()
tuple(x)
list(filter(lambda x: x == 1, [1,2,3]))

# Another example
filter(lambda x: x < 0, range(-5, 5))
list(filter(lambda x: x < 0, range(-5, 5)))


# Other methods for lists
x = [3,6,1,2,8,3,5,7]
# Reverse, don't need assignment
x.reverse() 
x
# Sort a list, don't need assignment
x.sort() 
x
# Append elements
x.append([10, 12, 14])
x
# Extend a list
x.extend([11, 12, 14])
x
# Insert in a specific position
x.insert(1,'+')
x
# Remove first occurrence
x.remove('+')  #Removes the first occurrence '+'
x

# enumerate():
# adds a counter to an iterable and 
# returns it in a form of enumerate object

import string # to get the letters from the alphabet

# Example:
y = [3,1,2,5,2]
enumerate(y)
list(enumerate(y))

# List with letters
letters = list(string.ascii_lowercase)
letters

# each item is a tuple
for item in enumerate(letters):
	print(item)

# iterate with elements of a tuple
for number, letter in enumerate(letters):
	print("%s is the letter with index %s" %(letter,number))


#---------- Dictionary ----------#

# We can use zip with to create dictionaries
d = dict(zip(letters,range(1,27)))
d['a']
d.keys() #Don't expect order!
d.values() 
d.items()

# iterate through items()
for key, value in d.items():
	if value == 1:
		print(key)

for k, v in d.items():
	print("%s is the letter number %s" %(k, v))

# Add a new instance
newletter = {'A': 27}
d.update(newletter)
d

# Overwrite a value
new_a_value = {'a':'first'}
d.update(new_a_value) 
d

# Or:
d['z'] = 'last' ## overwrites
d

# Update using a list of values
u = {"A" : [29, 30, 27]}
d.update(u)
d

#---------- For/else ----------#

# What is happening here?
for i in range(1,20):
	if i % 5 == 0:
		print(i)		
else:
	print('print this')
print('this other thing')

# And here?
for i in range(1,20):
	if i % 5 == 0:
		print(i)
		break		
else:
	print('print this')	
print('this other thing')

# Our find_prime() from yesterday:
def find_primes(me = 121, primes = []):
    if me == 2:
    	primes.append(2)
        return primes

    for i in range(2, me):
    	if me % i == 0:
        	break
    else:
    	primes.append(me) # Only executes if the loop does not break
    return find_primes(me-1, primes) # Always executes
find_primes(me = 10)

#---------- Debugging ----------#

import pdb # to debug the function

def squared_num(num):
	print('Find the Answer')
	r = num**2
	return r

def print_squared(num):
	pdb.set_trace()
	print('call squared_num')
	answer = squared_num(num = num)
	return answer

# Basic Commands:
# c: continue execution
# w: shows the context of the current line it is executing.
# a: print the argument list of the current function
# s: Execute the current line and stop at the first possible occasion.
# n: Continue execution until the next line in the current function is reached or it returns.
# s vs. n: with s, we see the step in the nested function, 
#        with n, we only see the steps in the current function

print_squared(2)

# Find more here: https://book.pythontips.com/en/latest/debugging.html


#---------- Tree ----------#

# Tree is a binary data structure:
# Example:
# https://www.cdn.geeksforgeeks.org/wp-content/uploads/binary-tree-to-DLL.png
# It contains our data, and left/right child (nodes)

# Create Class Node:
class Node():
	def __init__(self, value = None):
		self.value = value
		self.parent = None
		self.children = [None, None]			
		
	def __repr__(self):
		return "Node object with value %s" %(self.value)
		
	def __str__(self):
		if self.children != (None,None):
			return "Node value: %s \n left child: \n %s \n right child: \n %s" %(self.value,self.children[0],self.children[1])
		else: return "Node value: %s" % self.value	

#Create Class Tree:
class Tree():
	def __init__(self, root=None):
		self.root = root # First node
		self.branches = [[root]] # All branches. 
		# We use [[]] because we want to make the object root
		# in a list. But, we also want to make root a list.
		
	def add_branch(self, node, children):
		node.children = children # update object node
		for branch in self.branches: # get branches from the object node
			if branch[-1] == node: # check the last node in a given branch is each to the node
								   # if we find a match, we add the children to the correct place
				newbranch = branch + [children[0]]
				newbranch2 = branch + [children[1]]
				self.branches.append(newbranch)
				self.branches.append(newbranch2)
				self.branches.remove(branch)



# Create Nodes
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node1 # representation of the object
print(node1) # print node1

# Start tree
mytree = Tree(root = node1)
mytree.branches # Check branches
mytree.add_branch(node = node1, children = [node2, node3]) # nodes 2 and 3 are children of node 1
mytree.add_branch(node = node2, children = [node4, node5]) # nodes 4 and 5 are children of node 2
mytree.root # Check root
mytree.branches # Check branches

print(node1) # print node1
print(node2) # print node2
print(node3) # print node3


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