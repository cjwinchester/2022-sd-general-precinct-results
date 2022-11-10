import time
import random

import requests
from bs4 import BeautifulSoup

start_page = 'https://electionresults.sd.gov/ResultsList.aspx?type=CTYALL'

r = requests.get(start_page)
r.raise_for_status()

soup = BeautifulSoup(r.text, 'html.parser')
links = soup.find_all('div', {'class': 'county-export-listitem'})
county_links = [(x.text.strip(), f'https://electionresults.sd.gov/{x.a["href"]}') for x in links]

for link in county_links:
    county_name, url = link
    r = requests.get(url)
    r.raise_for_status()
    with open(f'pages/{county_name}.html', 'w') as outfile:
        outfile.write(r.text)

    print(f'Downloaded page for {county_name}')
    time.sleep(random.uniform(1, 2))
