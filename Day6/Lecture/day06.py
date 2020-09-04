# Python - 2020 Summer Course
# Day 6
# Topic: APIs
# Instructor: Patrick Cunha Silva
# Former Instructors: Ryden Buttler, Erin Rossiter
#                     Michele Torres, David Carlson, and
#                     Betul Demirkaya
# First Instructor: Matt Dickenson

import os
os.chdir('/Users/pcunhasilva/Dropbox/PythonClass/Summer2020/Day6/Lecture')

#---------- APIs ----------#

# API stands for:
# 	- Application (a piece of software, a computer program, or a server) 
# 	- Programming (what you’re doing with python)
# 	- Interface (how you’re communicating)


# How It Works:
# 	- Every Internet page is stored on a remote server
# 	- When you go to a website, a request goes out to their remote server
# 	- Your browser (the client) receives the response
# 	- When surfing the web, the API is the part of the remote server 
#	  that receives requests and sends responses
# 	- Informative explanation: 
#	  https://towardsdatascience.com/what-is-an-api-and-how-does-it-work-1dccd7a8219e

# How Developers Use It: 
# 	- The app’s functionality requires photography (think SnapChat)
# 	- iPhone devs already made camera software & efficient translations of inputs to outputs
# 	- Devs can use that software instead of writing it from scratch! (gains from trade)
# 	- Use the iPhone camera API to embed photography functions in your app
# 	- When Apple upgrades the camera software, your app benefits from the improvements
# 	- Another non-technical explanation: https://www.howtogeek.com/343877/what-is-an-api/


# How We (social scientists) Use It
# 	- Tools:
#		1 - Google Cloud Speech API
#		2 - Microsoft Azure Emotion API

# 	- Data:
#		1 - Twitter
#		2 - GoogleMaps
#		3 - Census
#		4 - FEC
#		5 - Google Civic API
#		6 - Legislative data (ex. UK and Brazil Parliaments)


# All APIs are different, and each has its own learning curve 
# Some require account keys:
# 	- Keep these private
# Most have request limits
# Some aren’t free
# We’re using python wrappers for APIs
# 	- R also offers API wrappers
# 	- Look for these to ease your coding burden




#---------- Pollster API ----------#

# http://elections.huffingtonpost.com/pollster/api/v2
# pip3 install pollster

# adapted from example.py at https://github.com/huffpostdata/python-pollster
# more information here: https://app.swaggerhub.com/apis/huffpostdata/pollster-api/2.0.0

import datetime # to format date
import webbrowser # to open our browser
import pollster # API wrapper

# Start the API
api = pollster.Api()

# not sure what a tag is!
tags = api.tags_get() ## list of dictionary-looking objects

# check out the slugs, anyway
for t in tags:
	print(t.slug)
# slug is a unique identifier 

# 2016 president looks good
charts = api.charts_get(tags = '2016-president')
len(charts.items) # 50 charts

# what's in a single chart (aka plot)
charts.items[0]

# navigate through it....
charts.items[0].question.name

# let's check out their plot
webbrowser.open(charts.items[0].url)


# We want to find the first question that was asked at more than 30 times
# The next() function returns the next item from the iterator. 
# It will stop when it finds the first question with at least 31 instances 
question_slug = next(c.question.slug for c in charts.items if c.question.n_polls > 30)

# We could also use it, but it is less efficient
question_slug2 = [c.question.slug for c in charts.items if c.question.n_polls > 30][0]


# grab polls with get request that matches our question_slug 
polls = api.polls_get(
  question = question_slug,
  sort = 'created_at'
)
polls

# Grabbing info from these polls
# How they were field? Internet, Phone?
[p.mode for p in polls.items]

# Get all chart slugs for charts built using this question
[p.poll_questions[0].question.charts for p in polls.items]

# first element in charts.item is a chart. we want its slug
# grab first one
chart_slug = charts.items[0].slug
trendlines = api.charts_slug_pollster_trendlines_tsv_get(chart_slug)
trendlines

# We can rearrange data too
by_date = trendlines.pivot(index='date', columns='label', values='value').sort_index(0, ascending=True)
by_date

# Now looking at question-level
questions = api.questions_get(
  tags='2016-president',                   # String | Comma-separated list of tag slugs (most Questions are not tagged)
  election_date=datetime.date(2016, 11, 8) # Date | Date of an election
)
questions

# and responses (question_slug is from above, as well)
question_slug
responses_clean = api.questions_slug_poll_responses_clean_tsv_get(question_slug)
responses_clean

#---------- Google Maps API ----------#


# pip install googlemaps

# Navigate to https://console.developers.google.com/apis/credentials?project=_
# Create a project, go to library, then enable geocoding and distance matrix APIs

import importlib # to import file
import sys # add directory to system PATH

# system PATH:
# The system path is a list of folders, separated by a semicolon, 
# that identifies the folders that the system should search when looking 
# for files that are called from the Run dialog box, command line, or other processes.
# Source: https://bit.ly/2Z4KAzP

# Add directory where your key is to system PATH
sys.path.insert(0, '/Users/pcunhasilva/Dropbox/Projects/Secrets/')

# Import items from file
imported_items = importlib.import_module('start_googleAPI')

# Copy client to an object named gmaps
gmaps = imported_items.client

# Locate the white house
whitehouse = 'The White House'
location = gmaps.geocode(whitehouse)
location # location is a list of dictionaries

# Get keys
location[0].keys()
# Get geometry
location[0]['geometry'].keys()
# Get location
location[0]['geometry']['location']

# Store latlong
latlong = location[0]['geometry']['location']

# Get the destination using latlong
destination = gmaps.reverse_geocode(latlong)

# sometimes you have to dig...
print(destination[0]["address_components"][2]['long_name'])

# Find Duke University
duke = gmaps.geocode('326 Perkins Library, Durham, NC 27708')
duke_loc = duke[0]['geometry']['location']
duke_loc

# Find WUSTL
washu = gmaps.geocode('1 Brookings Dr, St. Louis, MO 63130')
washu_loc = washu[0]['geometry']['location']
washu_loc

# Find the distance (in km) between Duke and WUSTL
distance = gmaps.distance_matrix(duke_loc, washu_loc)
print(distance['rows'][0]['elements'][0]['distance']['text'])

# Plotting in Google Maps
# More information on https://github.com/vgm64/gmplot
# pip install gmplot

from gmplot import gmplot
google_key = imported_items.api_key

# Get St. Louis
STL = gmaps.geocode('St. Louis')
STL[0]['geometry']['location']
latlongSTL = STL[0]['geometry']['location']

# Create plot area
plot1 = gmplot.GoogleMapPlotter(lat = latlongSTL['lat'], lng = latlongSTL['lng']
	, zoom = 13, apikey = google_key)

# Create an object with places in STL
stl_places = ["Forest Park, St. Louis",
	"Missouri Botanical Garden, St. Louis",
	"Anheuser Busch, St. Louis",
	"Arch, St. Louis"]

# Create a function to find latlong for stl_places
def grab_latlng(place):
	x = gmaps.geocode(place)
	return (x[0]["geometry"]["location"]["lat"], x[0]["geometry"]["location"]["lng"])

# Run the function
l = [grab_latlng(i) for i in stl_places]

# Use zip to assign lat and long to different objects
# zip(* ) means that the object l will be unpacked, 
# making each of its elements a separate argument
attraction_lats, attraction_lons = zip(*l)
attraction_lats
attraction_lons

# Add points to our plot
plot1.scatter(lats = attraction_lats, lngs = attraction_lons,
	'black',
	size = 40,
	marker = True)

# Draw the plot
plot1.draw("my_map.html")


#---------- Twitter API ----------#

# pip install tweepy
import tweepy
# http://docs.tweepy.org/en/v3.8.0/api.html

twitter = importlib.import_module('start_twitter')
api = twitter.client

# See rate limit
limit = api.rate_limit_status()
limit.keys() ##look at dictionary's keys
# prepare for dictionaries all the way down

limit["resources"] ## another dictionary
limit["resources"].keys()
limit["resources"]["tweets"] ## another dictionary!!

for i in limit["resources"]["tweets"].keys():
	print(limit["resources"]["tweets"][i]) ## another dictionary!

# Create user objects
don = api.get_user('realDonaldTrump')
don # biiiig object 

# Check type and methods
type(don)
dir(don)

# Trying some of these methods
print(don.id)
print(don.name)
print(don.screen_name)
print(don.location)

# Check his tweets
don.status # last tweet
don.status.text # text
don.status._json # .json file
don.statuses_count # tweet ID

# Check his number of followers
don.followers_count

# Gives back user objects
don_20 = don.followers() ## only the first 20!
don_20
len(don_20)

# Screen names
[f.screen_name for f in don_20]

# up to 200 (limit)
don_200 = api.followers(don.id, count = 200) ## up to 200
[f.screen_name for f in don_200]
len(don_200)

# A more round-about way, look up each user
don_5000 = don.followers_ids() #creates a list of user ids - up to 5000
len(don_5000)

# Get followers geo location
for follower_id in don.followers_ids()[0:50]:
	user = api.get_user(follower_id)
	if user.location == '':
		print('Not available')
	else: 
		print(user.location)

# Normally count = 200 is limit, let's go around that.

# By default, each method returns the first page, 
# which usually contains a few dozen items.
# We can define the pagination manually to get more results
don_statuses = []
for p in range(1, 10):
	# extend gets the entire tweet
	don_statuses.extend(api.user_timeline(id = 'realDonaldTrump', page = i, count = 20))
don_statuses
len(don_statuses)

# How was it tweeted?
source = [x.source for x in don_statuses]
source

# Print tweets with source equal to iPhone
[x.text for x in don_statuses if x.source == "Twitter for iPhone"]


# Cursor performs pagination easily for you
# iterate through the first 20 statuses in the timeline
histweets20 = [] ## tweet objects
for status in tweepy.Cursor(api.user_timeline, id = 'realDonaldTrump').items(20):
    histweets20.append(status)    
len(histweets20)

# iterate through all of the status 
histweets = [] ## tweet objects
for status in tweepy.Cursor(api.user_timeline, id = 'realDonaldTrump').items():
    histweets.append(status)
len(histweets) # for some weird reason, it is returning a random number of status

# You should definitely hit the rate limit here.....
hisfollowers = []
for item in tweepy.Cursor(api.followers_ids, 'realDonaldTrump').items():
	hisfollowers.append(item)
len(hisfollowers)

#---------- Spotify API ----------#

# pip install spotipy
import spotipy
# https://spotipy.readthedocs.io/en/2.14.0/


# Start API
credentials = importlib.import_module('start_spotify')
sp = spotipy.Spotify(client_credentials_manager=credentials.client_credentials)

# Search for an artist
taylor = sp.artist('06HL4z0CvFAxyc27GXpf02') #artist query

# check type and methods
type(taylor)
dir(taylor)

# Check Keys
taylor.keys()

# Check Popularity (What does it mean?)
taylor['popularity']
# https://developer.spotify.com/documentation/web-api/reference/artists/get-artist/

# Check Followers
taylor['followers']

# We can also use search
name = "Daft Punk" #chosen search
result = sp.search(name, type = 'artist') # Valid types are: album , artist, playlist, track, show and episode

# check type and methods
type(result)
dir(result)

# Check Keys
result.keys()

# Get the number of results
len(result['artists']['items'])

# Print artist
for i in range(len(result['artists']['items'])):
	print(result['artists']['items'][i]['name'])

# Search for track to get audio features
one = sp.audio_features('0DiWol3AO6WpXZgp0goxAV')

# Check audio features
one[0]


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