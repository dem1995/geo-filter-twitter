# geo-filter-twitter
Program for filtering a collection of tweets geographically. More specifically, this program allows filtering tweets based on them being in some specified radii of some collection of locations.

## Configuration
The program uses a configuration file with radii and locations for filtering.

To get started, after installing dependencies, just modify [`preparation-input_cities.txt`](preparation-input_cities.txt) with the locations (in any format you think a Google Maps search would likely find reasonable) and radii (in miles) about the locations' centers that you want to consider.

Afterwards, run [`preparation-generation_script.sh`](preparation-generation_script.sh). This automatically prepares an actual filtering script, `generate_datasets.sh`, for running.

## Running
To run the filters, after configuration perform `sh generate_datasets.sh <input_tweet_file_name.jsonl input_tweet_file_name2.jsonl ...>`, which will create a folder for each input file and within each of those put filter results (as jsonl files) with filenames that contain information about the corresponding filter location/radius.

## Example Run
`// Make sure you have a Python environment with the required libraries, if you don't already`\
`pip install -r requirements.txt`\
`// Modify preparation-input_cities.txt`\
`sh preparation-generation_script.sh`\
`sh generate_datasets.sh input1.jsonl input2.jsonl ... inputn.jsonl`\
`// The end result is a set of output folders with corresponding filter outputs inside of them`
