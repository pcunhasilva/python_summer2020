import googlemaps
import sys
import importlib

# Add directory where your key is to system PATH
sys.path.insert(0, '/Users/pcunhasilva/Dropbox/Projects/Secrets/')

# Import items from file
imported_items = importlib.import_module('start_googleAPI')

gmaps = imported_items.client

# Define White House
whitehouse = '1600 Pennsylvania Avenue, Washington, DC'

# Which embassy is closest to the White House in meters? how far?
# Define embassies
embassies = [[38.917228,-77.0522365],
	[38.9076502, -77.0370427],
	[38.916944, -77.048739]]

print ("Let's find the closest embassy to the WH.")
def distance(depart, destines):
    dis =  gmaps.distance_matrix(depart, embassies)
    return dis

def close_far(dis, closest = True):
    km = []
    for i in range(0, len(dis['destination_addresses'])):
        km.append(float(dis['rows'][0]['elements'][i]['distance']['text'].split(" ")[0]))
    if closest == False:
    	maxIndex = km.index(max(km))
    	return """Farthest Embassy Address: %s.\nDistance to the WH: %sm""" % (dis['destination_addresses'][maxIndex], max(km) * 1000)
    else:
    	minIndex = km.index(min(km))
    	return """Closest Embassy Address: %s.\nDistance to the WH: %sm""" % (dis['destination_addresses'][minIndex], min(km) * 1000)

# Find distances
dis = distance(whitehouse, embassies)

# 1) which of these embassies is closest to the White House in meters? 
print(close_far(dis))

# 2) if I wanted to hold a morning meeting there, which cafe would you suggest?
breakfastpalce = gmaps.places_nearby(embassies[1], keyword = 'breakfast',
                min_price = 3, max_price = 5, type = 'cafe',
                rank_by = "distance")
print ("Get the name of the place:")
print (breakfastpalce['results'][0]['name'])
print ("Get the rating of the place:")
print (breakfastpalce['results'][0]['rating'])
print ("Get the address of the place:")
print (breakfastpalce['results'][0]['vicinity'])

# 3) if I wanted to hold an evening meeting there, which bar would you suggest? 
bars = gmaps.places('bars near ' + '1617 Massachusetts Ave NW, Washington, DC 20036, USA')
rates = []
for i in range(0, len(bars)):
    rates.append(bars['results'][i]['rating'])
print ("This is the best bar: %s." % bars['results'][rates.index(max(rates))]['name'])
print ("The bar rating is: %s." % bars['results'][rates.index(max(rates))]['rating'])
print ("And it is located at: %s" % bars['results'][rates.index(max(rates))]['formatted_address'])

