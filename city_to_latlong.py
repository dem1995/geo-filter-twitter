"""
Program that takes in an address and returns the coordinates
"""
import argparse
from geopy.geocoders import Nominatim

if __name__ == '__main__':
	geolocator = Nominatim(user_agent="filter-latlong.py")
	parser = argparse.ArgumentParser(description=__doc__)
	parser.add_argument(
		'input', metavar='I',
		help='Any reasonable format for a city. Ambiguous cases will default to a more-prominent city')
	args = parser.parse_args()
	_, coords = geolocator.geocode(args.input)
	print(coords)
