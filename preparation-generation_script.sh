#!/bin/sh
# Script to generate a list of tweet datasets centered around coordinates provided by a file.

#Default city radius to consider
RADIUS=80
#Clear the generate_dataset script
cat /dev/null > generate_datasets.sh

#For each line that does not start with # in the config file, read the line in and...
sed '/^#/ d' < preparation-input_cities.txt | while IFS= read -r LINE || [ -n "$LINE" ];
do
	#If the line that was read in was a number, it is to be used as a radius about locations for filtering
	if echo $LINE | egrep -q '^([0-9]+(\.[0-9][0-9]?)?)'; then
		RADIUS=$(echo $LINE | sed -e 's/\r//g')
	#Otherwise, the line is the location name itself that will be used for filtering
	else
		COORDS="$(python city_to_latlong.py "$LINE")"
		VALID_FILENAME=$(echo "$LINE" | sed -e 's/[^A-Za-z0-9_-]/_/g')
		echo "python filter_latlong_radius.py tests/out_test.jsonl '"$COORDS"' "$RADIUS" > "$VALID_FILENAME"_"$RADIUS".jsonl" >> generate_datasets.sh
	fi
done
