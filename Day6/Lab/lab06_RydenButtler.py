# pip install googlemaps
#https://console.developers.google.com/apis/credentials?project=_
#need maps and distance APIs enabled
import googlemaps
import imp
import sys

sys.path.insert(0, '/Users/ryden/Dropbox/Coding/Secrets')
imported_items = imp.load_source('goog', '/Users/ryden/Dropbox/Coding/Secrets/start_google.py')

gmaps = imported_items.client

whitehouse = '1600 Pennsylvania Avenue, Washington, DC'

embassies = [[38.917228,-77.0522365], 
	[38.9076502, -77.0370427], 
	[38.916944, -77.048739] ]

# function to evalute distance between two places
def dists(origin, place_list):
	distances = []
	if type(origin) != str:
		origin = gmaps.reverse_geocode(origin)[0]['geometry']['location']
	for place in place_list:
		latlng = gmaps.reverse_geocode(place)[0]['geometry']['location']
		dist = gmaps.distance_matrix(origin, latlng)
		distances.append(dist['rows'][0]['elements'][0]['distance']['value'])
	return distances

# function to determine nearest location among set
def nearest(place, others):
	lengths = dists(place, others)
	smallest = min(lengths)
	match = lengths.index(smallest)
	return match

# function to find a place in Google maps
def find_place(place_list):
	places = []
	for place in place_list:
		places.append(gmaps.reverse_geocode(place)[0]['formatted_address'])
	return places

# function to determine nearest venue
def nearest_venue(original_location, other_locations, venue_type):
	nearby = nearest(original_location, other_locations)
	embassy = other_locations[nearby]
	search = gmaps.places(query = venue_type, location = embassy)['results']
	venues = []
	for i in search:
		loc = i['geometry']['location']
		coords = [loc['lat'], loc['lng']]
		venues.append(coords)
	near_venue = nearest(embassy, venues)
	return str(search[near_venue]['name'])


# TODO: write code to answer the following questions: 
# 1) which of these embassies is closest to the White House in meters? 
# how far is it, and what is the address?
emb = nearest(whitehouse, embassies)

# 2) if I wanted to hold a morning meeting there, which cafe would you suggest?
cafe = nearest_venue(whitehouse, embassies, 'cafe')

# 3) if I wanted to hold an evening meeting there, which bar would you suggest? 
bar = nearest_venue(whitehouse, embassies, 'bar')

