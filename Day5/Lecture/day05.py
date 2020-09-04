# Python - 2020 Summer Course
# Day 5
# Topic: Regular Expressions and Naive Bayes Classifier
# Instructor: Patrick Cunha Silva
# Former Instructors: Ryden Buttler, Erin Rossiter
#                     Michele Torres, David Carlson, and
#                     Betul Demirkaya
# First Instructor: Matt Dickenson

# Set Directory
import os
os.chdir('/Users/pcunhasilva/Dropbox/PythonClass/Summer2020/Day5/Lecture')


#---------- Regular Expressions ----------#

# Regular expressions are useful to extract information from text.
# Set of “rules” to identify or match a particular sequence of characters.
# Most text in ASCII: letters, digits, punctuation and symbols 
# (but unicode can also be used)
# In Python, mainly through library re.

import re

# Load example text 
# read in example text, remember:
# readlines makes a list of each line break in file
with open("obama-nh.txt", "r") as f:
  text = f.readlines()


# How is this file structured?
# How does it impact our 'text' object?
print(text[0:3])
print(text[0])
print(text[1])
print(text[2])

# Join into one string
# What could we have done at the outset instead?
alltext = ''.join(text) 

# OR
with open("obama-nh.txt", "r") as f:
  alltext = f.read()


# Useful functions from re module:

# re.findall: Return all non-overlapping matches of pattern 
#             in string, as a list of strings
# re.split: Split string by the occurrences of pattern.
# re.match: If zero or more characters at the beginning of 
#           string match the regular expression pattern, 
#           return a corresponding match object.
# re.search: Scan through string looking for the first location where 
#            the regular expression pattern produces a match, 
#            and return a corresponding match object.
# re.compile: Compile a regular expression pattern into a regular 
#             expression object, which can be used for matching using i
#             ts match(), search() and other methods

# See https://docs.python.org/3/library/re.html for more.


# Examples
re.findall(r"Yes we can", alltext) # All instance of Yes we can
re.findall(r"American", alltext) # All instances of American
re.findall(r"\n", alltext) # all breaklines

# we use "r" to signal the start of a pattern.
# "r" is Python's raw string notation for regular expression patterns
# used instead of escape character "\" 
"\n"
print("\n")

"\\n"
print("\\n")

r"\n"
print(r"\n")

r"\\n"
print(r"\\n")

#---------- Basic special characters ----------#

# \d digits
re.findall(r"\d", alltext) 
# \D non-digits
re.findall(r"\D", alltext) 
# all instances of the char in []
re.findall(r"[a]", alltext) 
# all instances of the from char 1 to char 2 in []
re.findall(r"[a-d]", alltext) 
# all char, ^ except for of the from char 1 to char 2 in []
re.findall(r"[^a-d]", alltext) 
# all char and digits (alphanumeric)
re.findall(r"[a-zA-Z0-9]", alltext) 
# \w alphanumeric, one word char 
re.findall(r"\w", alltext) # same as re.findall(r"[a-zA-Z0-9]", alltext)
# \W non-alphanumeric, one non-word char
re.findall(r"\W", alltext) # same as re.findall(r"[^a-zA-Z0-9]", alltext)
# \s whitespace
re.findall(r"\s", alltext) 
# \S non-whitespace
re.findall(r"\S", alltext) 
# . any char (include white spaces)
re.findall(r".", alltext) 
# \ is an escape character (. has a special use)
re.findall(r"\.", alltext) 


# all digits
re.findall(r"\d", alltext) 
# Match succeeds independently of the presence of the search string
re.findall(r"\d*", alltext).remove('') 
# r = re.findall(r"\d*", alltext)
# while '' in r:
  # r.remove('')
# r  
# At least one occurrence for the match to succeed ( 1 or many)
re.findall(r"\d+", alltext)
# Makes the preceding item optional. 
re.findall(r"\d?", alltext) 
# {x} exactly x times (numbers with exact number of digits)
re.findall(r"\d{3}", alltext) 
re.findall(r"\d{2}", alltext) 
re.findall(r"\d{1}", alltext) 
# {x, y} from x to y times (numbers with exact number of digits from x to y)
re.findall(r"\d{1,3}", alltext) 

# More here: https://www.regular-expressions.info/refrepeat.html
# And hear: https://www.debuggex.com/cheatsheet/regex/python

# Short Exercise: How would we grab 10/10 as it appears in text?
x = "Hi 10/10 hello 9/18 asdf 9/9"












# Answer
re.findall(r"\d{2}/\d{2}", x) 


## Explain what's happening:
x = "American's lov\we McDonalds"
re.findall(r"\w", x) 
# \w is Regular Expression Character Classes
x
# We need to add a escape
re.findall(r"\\w", x) 

# get any word that starts with America
re.findall(r"America[a-z]*", alltext) 

# get any complete word starting with an upper-case letter
re.findall(r"([A-Z]+\w*)", alltext) 
# () group of characters 
# starting with a letter A to Z
# + the next n characters

#---------- re.split() ----------#

# splits at digits, deletes digits
re.split(r'\d', alltext) 

# splits at non-digits, deletes char
re.split(r'\D', alltext) 

# What is this doing?
re.split(r'\.', alltext) # remove separator
re.split(r'(\.)', alltext) # using () we split and keep separator


#---------- re.compile() ----------#

# compile the regular expression as an object
# then the regular expression has methods!
keyword = re.compile(r"America[a-z]*")


# search file for keyword in line by line version
for i, line in enumerate(text):
  if keyword.search(line):
  	print(i)
    print(line) 
# enumerate() allows us to loop over something and have an automatic counter

# Create a regex object
pattern = re.compile(r'\d')
pattern.findall(alltext)
pattern.split(alltext)

# Can also search across lines in single strings with re.MULTILINE
mline = 'bin\nban\ncan'
print(mline)

# ^ check the start of the string
# looking for b
pattern = re.compile(r'^b\w*') # "^" words starting in b of any size
pattern.findall(mline)

# looking for b in multilines
pattern = re.compile(r'^b\w*', re.MULTILINE)
pattern.findall(mline)

# Now, back to the speech as a single string...
# Explain the difference between these two lines
re.findall(r'^b\w*', alltext, re.MULTILINE)
re.findall(r'^b\w*', alltext)

# re.MULTILINE treats each line as its own string
# for the sake of the pattern


# Short Exercise
# Check if a line ends in a period
# How is this working?
re.findall(r'^.*\.$', alltext, re.MULTILINE)
# '^.' = starts with any char
# * returns up to the end of the line
# \. if the line has a period
# $ if the line ends with a period


#---------- search, match, and groups ----------#
t = '12 twelve'

# find a number and a word separated by a whitespace
pattern = re.compile(r'(\d*)\s(\w*)')
# create an instance
tsearch = pattern.search(t) 
# tuple of all groups
tsearch.groups() 
# the complete match
tsearch.group(0) 
# the first group
tsearch.group(1) 
# the second group
tsearch.group(2) 

# Similar to using () alone, but the text
# matched by the group is then accessible
# (?P<Y>...)  Capturing group named Y
pattern = re.compile(r'(?P<number>\d*)\s(?P<name>\w*)')
tsearch = pattern.search(t)
tsearch.groups()
tsearch.groupdict()

# Another example
mytext = '12 24'
pattern = re.compile(r'(\d*)\s(\d*)')
pattern.search(mytext).groups()
pattern.search(mytext).group(0)
pattern.search(mytext).group(1)
pattern.search(mytext).group(2)


# match starts search at beginning of string
# like an invisible ^
pattern.match(r"12 24").groups()
pattern.match(r"a12 24").groups()



#---------- Naive Bayes ----------#
# Some docs for this library: 
# http://nltk.org/api/nltk.classify.html#module-nltk.classify.naivebayes

 # pip install nltk
import nltk
nltk.download('names')
from nltk.corpus import names
import random

# Create a list of tuples with names
names = ([(name, 'male') for name in names.words('male.txt')] +
  [(name, 'female') for name in names.words('female.txt')])

# Now, we shuffle
random.shuffle(names)

# We need training and test sets.
# Define training and test set sizes
len(names) # N of observations
train_size = 5000

# Split train and test objects
train_names = names[:train_size]
test_names = names[train_size:]

# A simple feature: Get the last letter of the name
def g_features1(word):
  return {'last_letter': word[-1]}

# Msc:
def return_two():
  return 5, 10

# When a method returns two values, we can use this format: 
x, y = return_two()

# Loop over names, return tuple of dictionary and label
train_set = [(g_features1(n), g) for (n, g) in train_names]
test_set = [(g_features1(n), g) for (n,g) in test_names]

# Run the naive Bayes classifier for the train set
classifier = nltk.NaiveBayesClassifier.train(train_set)

# Apply the classifier to some names
classifier.classify(g_features1('Neo'))
classifier.classify(g_features1('Trinity'))
classifier.classify(g_features1('Max'))
classifier.classify(g_features1('Lucy'))

# Get the probability of female:
classifier.prob_classify(g_features1('Lucy')).prob("female")


# Check the overall accuracy with test set
print(nltk.classify.accuracy(classifier, test_set))

# Lets see what is driving this
classifier.show_most_informative_features(5)


# Lets be smarter
# What all are we including now?
def g_features2(name):
  features = {}
  features["firstletter"] = name[0].lower()
  features["lastletter"] = name[-1].lower()
  for letter in 'abcdefghijklmnopqrstuvwxyz':
      features["count(%s)" % letter] = name.lower().count(letter)
      features["has(%s)" % letter] = (letter in name.lower())
  return features

# Test function
g_features2('patrick')

# Run for train set
train_set = [(g_features2(n), g) for (n,g) in train_names]

# Run for test set
test_set = [(g_features2(n), g) for (n,g) in test_names]

# Run new classifier
classifier = nltk.NaiveBayesClassifier.train(train_set)

# Check the overall accuracy with test set
print(nltk.classify.accuracy(classifier, test_set))

# Lets see what is driving this
classifier.show_most_informative_features(5)


# Worse? Better? How can we refine?
# Lets look at the errors from this model
# and see if we can do better
errors = []
for (name, label) in test_names:
  guess = classifier.classify(g_features2(name))
  if guess != label:
    prob = classifier.prob_classify(g_features2(name)).prob(guess)
    errors.append((label, guess, prob, name))


for (label, guess, prob, name) in sorted(errors):
  print('correct={} guess={} prob={:.2f} name={}'.format(label, guess, prob, name))


# What should we do here?
def g_features3(name):
  features = {}
  if name[-2:] == "ie" or name[-1] == "y":
    features["last_ie"] = True
  else:
    features["last_ie"] = False
  if name[-1] == "k":
    features["last_k"] = True
  else:
    features["last_k"] = False

  return features

train_set = [(g_features3(n), g) for (n,g) in train_names]
test_set = [(g_features3(n), g) for (n,g) in test_names]
classifier = nltk.NaiveBayesClassifier.train(train_set)
print(nltk.classify.accuracy(classifier, test_set))


# Now lets look at some bigger documents
from nltk.corpus import movie_reviews
nltk.download('movie_reviews')

# list of tuples
# ([words], label)
documents = [(list(movie_reviews.words(fileid)), category)
              for category in movie_reviews.categories()
              for fileid in movie_reviews.fileids(category)]
random.shuffle(documents)


# Dictionary of words and number of instances
all_words = nltk.FreqDist(w.lower() for w in movie_reviews.words())
len(all_words)
word_features = [k for k in all_words.keys() if all_words[k] > 5]

# Check the frequency of ','
all_words[',']
# Print frequency of all words
for w in word_features:
  print(all_words[w])

# Function to get document features
def document_features(document):
  document_words = set(document)
  features = {}
  for word in word_features:
      features['contains(%s)' % word] = (word in document_words)
  return features

print(document_features(movie_reviews.words('pos/cv957_8737.txt')))

## Now we have tuple of ({features}, label)
train_docs = documents[:500]
test_docs = documents[1000:1500]
train_set = [(document_features(d), c) for (d,c) in train_docs]
test_set = [(document_features(d), c) for (d,c) in test_docs]
classifier = nltk.NaiveBayesClassifier.train(train_set)

print(nltk.classify.accuracy(classifier, test_set[:50]))

classifier.show_most_informative_features(10)



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





