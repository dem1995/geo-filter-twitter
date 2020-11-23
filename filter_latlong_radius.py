"""
Program for filtering a collection of tweets based on their location of posting on Earth
"""
from math import cos, sqrt
import argparse
import json
import re
import sys
from typing import List
from geopy.distance import distance
from geopy.geocoders import Nominatim

def is_tweet_in_latlong_radius(tweet_json, latlong, radius):
	tweet_dict = json.loads(tweet_json)
	tweet_coords = None
	
	#Check whether coordinates are available or whether a valid place is available to approximate coordinates from
	coordinates_available = 'coordinates' in tweet_dict and tweet_dict['coordinates'] is not None
	place_available = ('place' in tweet_dict and tweet_dict['place'] is not None
			   and 'bounding_box' in tweet_dict['place']
			   and tweet_dict['place']['bounding_box'] is not None
			   and 'coordinates' in tweet_dict['place']['bounding_box']
			   and tweet_dict['place']['bounding_box']['coordinates'] is not None)
	
	#If coordinates are available in some form, use them as the tweet coordinates
	if coordinates_available:
		tweet_coords = tweet_dict['coordinates']['coordinates']
	elif place_available:
		tweet_bounding_box = tweet_dict['place']['bounding_box']['coordinates'][0]
		tweet_bb_centroid_longitude = sum(coord[0] for coord in tweet_bounding_box)/len(tweet_bounding_box)
		tweet_bb_centroid_latitude = sum(coord[1] for coord in tweet_bounding_box)/len(tweet_bounding_box)
		tweet_coords = [tweet_bb_centroid_longitude, tweet_bb_centroid_latitude]
	if tweet_coords is None:
		sys.stderr.write(f"Tweet coords is none. Ignoring offending tweet: {tweet_json}")
		return False
	
	#longitude is currently first due to how Twitter orders coordinates; we flip this now
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
