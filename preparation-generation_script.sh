#!/bin/sh
# Script to generate a list of tweet datasets centered around coordinates provided by a file.

RADIUS=40

while IFS= read -r LINE || [ -n "$LINE" ];
do
	COORDS="$(python city_to_latlong.py "$LINE")"
	VALID_FILENAME=$(echo "$LINE" | sed -e 's/[^A-Za-z0-9._-]/_/g')
	echo "python filter_latlong_radius.py tests/out_test.jsonl '"$COORDS"' "$RADIUS" > "$VALID_FILENAME"_"$RADIUS"" >> generate_datasets.sh
done < preparation-input_cities.txt
