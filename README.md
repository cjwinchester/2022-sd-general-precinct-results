# 2022 SD general election results
Some Python code to generate [a CSV file](sd-general-election-2022-precinct-unofficial-results.csv) with unofficial precinct-level results for the Nov. 8, 2022 general election in South Dakota.

Rather than try to parse the precinct spreadsheets generated for each county -- they're a mess -- this script instead downloads each county results page and, for each of them, assembles the endpoints for the API calls that grab the precinct data behind the scenes when you click the "Precinct Results" tabs for each race.

The three scripts:
- [`download.py`](download.py) downloads the HTML pages into the `/pages` directory
- [`scrape.py`](scrape.py) parses those files to assemble the API endpoints, then downloads JSON files for each race in each precinct into the `/data` directory
- [`process.py`](process.py) parses those JSON files into a single CSV file, [sd-general-election-2022-precinct-unofficial-results.csv](sd-general-election-2022-precinct-unofficial-results.csv)