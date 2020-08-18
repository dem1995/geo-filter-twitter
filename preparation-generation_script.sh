#!/bin/sh
# Script to generate a list of tweet datasets centered around coordinates provided by a file.

tmpfile=$(mktemp /tmp/abc-script.XXXXXX)

RADIUS=80
cat /dev/null > generate_datasets.sh
sed '/^#/ d' < preparation-input_cities.txt | while IFS= read -r LINE || [ -n "$LINE" ];
do
	if echo $LINE | egrep -q '^([0-9]+(\.[0-9][0-9]?)?)'; then
		RADIUS=$(echo $LINE | sed -e 's/\r//g')
	else
		COORDS="$(python city_to_latlong.py "$LINE")"
		VALID_FILENAME=$(echo "$LINE" | sed -e 's/[^A-Za-z0-9_-]/_/g')
		echo "python filter_latlong_radius.py tests/out_test.jsonl '"$COORDS"' "$RADIUS" > "$VALID_FILENAME"_"$RADIUS"" >> generate_datasets.sh
	fi
done
