## Go to https://polisci.wustl.edu/people/88/all OR https://polisci.wustl.edu/people/list/88/all
## Go to the page for each of the professors.
## Create a .csv file with the following information for each professor:
## 	-Specialization 
##  	Example from Deniz's page: https://polisci.wustl.edu/people/deniz-aksoy
##		Professor Aksoy’s research is motivated by an interest in comparative political institutions and political violence. 
## 	-Name
## 	-Title
## 	-E-mail
## 	-Web page

from bs4 import BeautifulSoup
import urllib
import csv
import os

# Set WD
os.chdir('/Users/pcunhasilva/Dropbox/PythonClass/Summer2020/Day4/Lab')

with open('lab04_patrick.csv', 'w') as f:
	w = csv.DictWriter(f, fieldnames = ("name", "title", "email", "website", "specialization"))
	w.writeheader()
	# Open the main website
	web_address = 'https://polisci.wustl.edu/people/list/88/all'
	web_page = urllib.request.urlopen(web_address)
	# Parse it
	soup = BeautifulSoup(web_page.read())
	# Find all faculty members
	fac = soup.find_all('article', class_ = 'faculty-post')
	# Loop over fac
	for i in fac:
		prof = {}
		# Name
		prof['name'] = i.h3.text
		# Title
		prof['title'] = i.find('ul').text.lstrip().rstrip()
		# Email
		prof['email'] = i.find(class_ = 'column contact').text.split(': ')[1]
		# Open prof website to get specialization
		try:
			faculty_page = urllib.request.urlopen("https://polisci.wustl.edu" + i.find('a')['href'])
			# webpage
			prof['website'] = "https://polisci.wustl.edu" + i.find('a')['href']
			# Parse it
			soup = BeautifulSoup(faculty_page.read())
		except urllib.error.URLError:
			prof['website'] = i.find('a')['href']
			prof['specialization'] = 'NA'
			continue
		# research interest
		try:
			prof['specialization'] = soup.find(class_ = 'post-excerpt').text
		except AttributeError:
			prof['specialization'] = 'NA'
		w.writerow(prof)



