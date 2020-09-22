# geo-filter-twitter
Metaprogram for filtering a collection of tweets based on their locations

## Configuration
The program uses a configuration file with radii and locations for filtering.

To get started, just modify [`preparation-input_cities.txt`](preparation-input_cities.txt) with the locations (in any format you think a Google Maps search would likely find reasonable) and radii (in miles) about the locations' centers that you want to consider.

Afterwards, run [`preparation-generation_script.sh`](preparation-generation_script.sh). This automatically prepares the actual filtering script, [`generate_datasets.sh`](generate_datasets.sh), for running.

## Running
To run the filters, after configuration perform `sh generate_datasets.sh <input_tweet_file_name.jsonl>`, which will put the filtered tweets into jsonl files with filenames that each contain information about the corresponding location specified and radius.

## Example Run
`// Modify preparation-input_cities.txt`\
`sh preparation-generation_script.sh`\
`generate_datasets.sh input1.jsonl input2.jsonl ... inputn.jsonl`\
