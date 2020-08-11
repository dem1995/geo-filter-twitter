"""
Program for filtering a collection of tweets based on their location of posting on Earth
"""
from math import cos, sqrt
import argparse
import elementally as elmy
from typing import List
from geopy.distance import distance
from geopy.geocoders import Nominatim

def is_tweet_in_latlong_radius(tweet_json, latlong, radius):
	tweet_dict = tweet_json.loads(tweet_dict)
	tweet_bounding_box = tweet_dict['coordinates']
	assert(tweet_bounding_box is not None)
	tweet_bb_sum = elmy.sum(tweet_bounding_box)
	tweet_bb_center = elmy.product(tweet_bounding_box, 1/len(bounding_box))
	tweet_distance = distance(tweet_bb_center, latlong)
	return tweet_distance.miles <= radius

#def centroid(List[])

geolocator = Nominatim(user_agent="filter-latlong.py")
print(geolocator.geocode("Saint-Louis, Canada").point)
_, coord2 = geolocator.geocode("saint louis")
_, coord1 = geolocator.geocode("toronto")
print(coord2)
print(coord1)
print(distance(coord1, coord2))

# if __name__ == "__main__":
# 	parser = argparse.ArgumentParser(desc=__doc__)


# 	print("Enter the city that you want to ")
