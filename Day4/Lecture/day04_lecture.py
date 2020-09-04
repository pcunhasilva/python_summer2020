# Python - 2020 Summer Course
# Day 4
# Topic: Web Scraping
# Instructor: Patrick Cunha Silva
# Former Instructors: Ryden Buttler, Erin Rossiter
#                     Michele Torres, David Carlson, and
#                     Betul Demirkaya
# First Instructor: Matt Dickenson

# Today's Topics:
#   1 - Urllib and Beautiful Soup
#   2 - Selenium
#   3 - Some tricks

# This is likely the most important day in the course.
# You will use all the modules here if you want to scrape the internet.



#---------- Overview ----------#

# 1 Call the website and open it
# 2 Extract the html code
# 3 Retrieve information using the names of the nodes, tags, ids, etc.
# 4 Store it in lists or directly to CSV files


#---------- Page Source ----------#

<!DOCTYPE html> <html>
<head>
<title >Page Title </title>
</head>
<body>

<h1>My first heading </h1>
<p>My first paragraph. </p>

</body> 
</html>

# Go to https://polisci.wustl.edu/people/88/ 
# Click right, then View Page Source

# See https://www.w3schools.com/tags/default.asp for a list wih HTML tags

#---------- Crawlers ----------#

# We (mainly) use two modules: urllib and BeautifulSoup

# pip3 install beautifulsoup4
from bs4 import BeautifulSoup
import urllib.request

# urllib:
# - web crawler
# - navigates to an url

# BeautifulSoup:
# - parses a downloaded HTML

# Useful when:
#   Info is contained in HTML (not served by JavaScript)
#   Encoded HTML follows predictable pattern
#   Example: https://www.presidency.ucsb.edu/documents/app-categories/press/press-briefings
#   Bad Example: https://www.oyez.org/cases/2017/17-586

# Example (WUSTL Political Science Webpage):

# Open a web page
web_address = 'https://polisci.wustl.edu/people/88/'
web_page = urllib.request.urlopen(web_address)
web_page

# Parse it
soup = BeautifulSoup(web_page.read())
print(soup.prettify()) # enable us to view how tags are nested in the document

# Find all cases of a certain tag 'a'
soup.find_all('a')
# Find all cases of a certain tag 'h3'
soup.find_all('h3')
# Returns a list... remember this!

# We can extract all text with a certain tag
fields = soup.find_all('h3') # list of html entries
[i.text for i in fields] # grab just the text from each one

# We can get all elements with the tag 'a.' Then, get the attributes
all_a_tags = soup.find_all('a')
all_a_tags[34].attrs  # returns a dictionary with the attributes

# Note: because all_a_tags is a list, we need to index the element.
# If we are interested in the first instance of the tag 'a,' we can use
soup.find('a')
soup.find('a').attrs 

# We can use a loop to get all the data
l = {"class" : [], "href" : []} # create a dictionary
for p in range(34,60):
  # try:
    # extract all attrs 'class' from the all_a_tags
    l["class"].append(all_a_tags[p].attrs["class"]) 
    # extract all attrs 'href' from the all_a_tags
    l["href"].append(all_a_tags[p].attrs["href"]) 
  # except KeyError:
    # continue
print(l)

# We can check all the attrs, using keys()
all_a_tags[34].attrs.keys()
all_a_tags[34]['href']
all_a_tags[34]['class']


# If we are interested only in the attributes 'class' and 'card' 
# nested within tag 'a', we can specific this in our first call:
soup.find_all('a', {'class' : "card"}) # returns a list

# It is very common that you will need to go level by level to access
# nested tags. Here is an example:
sections = soup.find_all('div') # get all tags 'div'
len(sections) # check the size of the object 
sections[2].a # FIRST 'a' tag within the 'div' tag OR:
sections[2].find('a') # FIRST 'a' tag within the 'div' tag
sections[2].find_all('a') ## ALL 'a' tags within the 'div' tag


# Creating a tree of objects. 
# We use it to get all data for on instance of 'div'
all_fields = soup.find_all('div')
randy = all_fields[34]

# heading
randy.find_all("h3") 

# Gives a list of all children (objects nested within the object)
randy.contents #

# Creates an iterator for children
randy.children # Remember: iterators are objects that we use in loops

# Print all nested elements within randy
for i, child in enumerate(randy.children):
  print("Child %d: %s" % (i,child))

# Siblings (Example):

# <html>
#   <body>
#       <a>
#         <b>
#          text1
#         </b>
#         <c>
#          text2
#         </c>
#       </a>
#   </body>
# </html>

# The <b> tag and the <c> tag are at the same level: 
# they’re both direct children of the same tag. 

# We can also print the next tag at the same level as the 'h3' tag
for sib in randy.next_siblings:
  print(sib)

# Or the previous instance
for sib in randy.previous_siblings:
  print(sib)
# What is happening?

# randy does not have previous siblings.
<article class="faculty-post"> 
<div class="image"> # randy = all_fields[34]
  <img alt="Headshot of Randall Calvert" src="URL"> # Children of randy
  <h3> # Children of randy
    <div> # all_fields[35]
      <span>Randall</span>
      &nbsp;
    </div>
    <div> # all_fields[36]
      <span>Calvert</span>
    </div>
  </h3>
</div>
<div class="dept">Academic Position # Next Sibling of randy
</div>

# all_fields[35] has a next sibling and all_fields[36] has a previous sibling
for sib in all_fields[35].next_siblings:
  print(sib)
for sib in all_fields[36].previous_siblings:
  print(sib)


# Beautiful Soup documentation
# http://www.crummy.com/software/BeautifulSoup/bs4/doc/


# Crawlers are incredibly fast, but also easier to detect and block
# You can incorporate some pauses to avoid detection
import random
import time

# Script will pause for a n seconds
time.sleep(random.uniform(1, 5))
print('Pause Ended')


#---------- Remote Driver ----------#

# Selenium is a “remote driver” of your favorite browser
# Therefore, you can pretty much simulate behavior of a human “surfing the web”
# With the right tricks, the likelihood of tracking and blocking your “bot” decreases.
# It also offers flexibility in terms of “unknown” items: 
#     you can even look by name of buttons in the page
# There are some downsides though...
#   - It is slower
#   - It is dependent on your internet connection quality


# Using Selenium: An Example

from selenium import webdriver
from bs4 import BeautifulSoup as bs
from selenium.webdriver.common.keys import Keys

# pip3 install selenium

# We will create a function to start our remote session
def start_chrome(webpage, silent = False):
    if silent == True:
      options = webdriver.ChromeOptions()
      options.add_argument("headless") # headless option
      driver = webdriver.Chrome(options = options)
    else:
      driver = webdriver.Chrome()
    driver.get(webpage)
    return driver

# Interactive example:
# start the web drivers
driver = start_chrome('https://www.google.com')
# find the seach element and enter text
search = driver.find_element_by_name('q')
search.send_keys('WUSTL Political Science')
# press Enter/Return
search.submit()
# We close the browser
driver.close()

#---------- Combining Approaches ----------#

# Example - Scraping Data from the Iceland Parliament:

# Define Webpage
url = "https://www.althingi.is/altext/cv/en/"

# Use a crawler to get all pages fr MPs
web_page = urllib.request.urlopen(url)
# Parse the HTML
soup = BeautifulSoup(web_page.read(), "html.parser") # html.parser severs as a basis for parsing text files in HTML format
# Get all urls
mps = soup.find('table').find_all('a', href = True)
mps
# Create objects to store the data:
page = []
name = []
party = []
email = []

# run the function for the first 2 cases
for i in range(0, 2):
  page.append(url + mps[i]['href'])
  driver = start_chrome(page[i], silent = True)
  html = driver.page_source
  driver.close()
  soup = BeautifulSoup(html)
  name.append(soup.find(class_ = 'article box news').find('h1').text)
  soup = soup.find(class_ = 'article box news').find('div', class_ = 'person')
  party.append(soup.find(class_ = 'office').find_all('li')[1].text)
  email.append(soup.find(class_ = 'contactinfo first notexternal').find('a', href = True)['href'].split(":")[1])


# More on Selenium:
# https://selenium-python.readthedocs.io/locating-elements.html


#---------- Reading and writing files ----------#

# 1 - Reading

import sys
import os

# Set WD
os.chdir('/Users/pcunhasilva/Dropbox/PythonClass/Summer2020/Day4/Lecture')

# Read all lines as one string
with open('readfile.txt') as f:
  the_whole_thing = f.read()
  print(the_whole_thing)


# Read line by line
with open('readfile.txt') as f:
  lines_list = f.readlines()
  for l in lines_list:
    print(l)

# More efficiently, we can loop over the file object
# (i.e. we don't need the variable lines)
with open('readfile.txt') as f:   
  for l in f:
    print(l)
    
    
# We can also manually open and close files,
# now we need to handle exceptions and close
# I never do this
f =  open('readfile.txt')
print(f.read())
f.close()

# Why not to do it manually?
# In any programming language, the usage of resources like file operations
# or database connections is very common. But these resources are limited in supply. 


# When a file is opened, a file descriptor 
# (a number that identifies an open file)
# is consumed which is a limited resource. 
# Only a certain number of files can be opened by a process at a time.
# In Python, it can be achieved by the usage of context managers 
# which facilitate the proper handling of resources.

# Example, not using with:
file_descriptors = [] 
for x in range(1000): 
    file_descriptors.append(open('readfile.txt')) 

# using with:
file_descriptors = [] 
for x in range(1000):
  with open("readfile.txt") as f:    
      data = f.read()
      file_descriptors.append(data)

# Source: https://www.geeksforgeeks.org/context-manager-in-python/ 

# 2 - Writing .txt

# Writing files is easy,
# We need to use the option 'w'
with open('test_writefile.txt', 'w') as f:
  ## wipes the file clean and opens it
  f.write("Hi guys.")
  f.write("Does this go on the second line?")
  f.writelines(['a\n', 'b\n', 'c\n'])

# We use 'a' to append new information to it
with open('test_writefile.txt', 'a') as f:
  f.write("I got appended!")

# See https://stackabuse.com/file-handling-in-python/ for more options


# 3 - Writing csv
import csv

# Open a file stream and create a CSV writer object
with open('test_writecsv.csv', 'w') as f:
  my_writer = csv.writer(f)
  for i in range(1, 100):
    my_writer.writerow([i, i-1])


# Now read in the csv
with open('test_writecsv.csv', 'r') as f:
  my_reader = csv.reader(f)
  mydat = []
  for row in my_reader:
    mydat.append(row)
print(mydat)

    
# Adding column names
with open('test_csvfields.csv', 'w') as f:
  my_writer = csv.DictWriter(f, fieldnames = ("A", "B"))
  my_writer.writeheader()
  for i in range(1, 100):
    my_writer.writerow({"B":i, "A":i-1})
    
# Reading the new file    
with open('test_csvfields.csv', 'r') as f:
  my_reader = csv.DictReader(f)
  for row in my_reader:
    print(row)

# We may find useful to save webpages for collecting data
def download_page(address, filename, wait = 5):
  time.sleep(random.uniform(0,wait))
  page = urllib.request.urlopen(address)
  page_content = page.read()
  if os.path.exists(filename) == False:
    with open(filename, 'wb') as p_html:
      p_html.write(page_content)
  else:
    print("Can't overwrite file " + filename)

download_page('https://polisci.wustl.edu/people/88/', "polisci_ppl.html")

# We can also parse a page that is saved on your computer
# Useful to scrape now, parse later.
with open('polisci_ppl.html') as f:
  myfile = f.read()
  soup = BeautifulSoup(myfile)
soup.prettify()


#---------- Scraping Tips ----------#

# Google Chrome is better to track nodes and page sources
# Inspect the source and get to know your document/website!
# Use the ’Copy Xpath’ command if you’re having troubles 
# (Find it in "Inspect" in Google Chrome)
# Use time breaks to avoid being blocked
# Check the Terms of Service (whether you obey them or not)


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

