"""
Program for filtering a collection of tweets based on their location of posting on Earth
"""
from math import cos, sqrt
import argparse
import json
import re
from typing import List
import elementally as elmy
from geopy.distance import distance
from geopy.geocoders import Nominatim

def is_tweet_in_latlong_radius(tweet_json, latlong, radius):
	tweet_dict = json.loads(tweet_json)
	tweet_coords = None
	coordinates_available = 'coordinates' in tweet_dict and tweet_dict['coordinates'] is not None
	place_available = 'place' in tweet_dict and tweet_dict['place'] is not None
	if coordinates_available:
		tweet_coords = tweet_dict['coordinates']['coordinates']
	elif place_available:
		tweet_bounding_box = tweet_dict['place']['bounding_box']['coordinates']
		tweet_bb_centroid = elmy.quotient(elmy.sum(tweet_bounding_box), [len(tweet_bounding_box)]*2)
		tweet_coords = tweet_bb_centroid
	assert(tweet_coords is not None)
	#longitude is currently first; this should be flipped
	tweet_coords = list(reversed(tweet_coords))
	tweet_distance = distance(tweet_coords, latlong)
	return tweet_distance.miles <= radius


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument(
		'input', metavar='I',
		help='A JSONL-formatted input file with lines of JSON-formatted tweets')
	parser.add_argument(
		'coordinates', metavar='C',
		help='The coordinates filtered tweets should be within, in latitude-longitude ordering. ' +
			 'May be written as (lat, long), [lat long], lat long, or any variation of these.')
	parser.add_argument(
		'radius', metavar='R', type=int,
		help='The radius, in miles, from the provided cooordinates that a Tweet must be within to ' +
			 'pass filtering.')
	args = parser.parse_args()

	coords = re.findall('-?\d+\.?\d*', args.coordinates)
	with open(args.input) as infile:
		for tweet_json in infile:
			if is_tweet_in_latlong_radius(tweet_json, coords, args.radius):
				print(tweet_json[0:-1])


# #def centroid(List[])

# geolocator = Nominatim(user_agent="filter-latlong.py")
# print(geolocator.geocode("Saint-Louis, Canada").point)
# _, coord2 = geolocator.geocode("saint louis")
# _, coord1 = geolocator.geocode("toronto")
# print(coord2)
# print(coord1)
# print(distance(coord1, coord2))

# if __name__ == "__main__":
# 	with open("out_test.jsonl") as infile:
# 		for line in infile:
# 			_, chicago = geolocator.geocode("chicago")
# 			print(is_tweet_in_latlong_radius(line, chicago, 10))

# # 	parser = argparse.ArgumentParser(desc=__doc__)


# # 	print("Enter the city that you want to ")
