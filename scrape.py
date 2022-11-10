import glob
import json
import random
import time

import requests
from bs4 import BeautifulSoup


html_files = sorted(glob.glob('pages/*.html'))
api_endpoint_fmt = 'https://sdresws.azurewebsites.net/ResultsAjax.svc/GetMapData?type={}&category=PREC&raceID={}&osn={}&county={}&party=0'

test = html_files[0]

def download_data_file(url, filename):
    r = requests.get(url)
    r.raise_for_status()

    datafile_path = f'data/{filename}'

    with open(datafile_path, 'w') as outfile:
        outfile.write(r.text)

    return datafile_path


for page in html_files:

    with open(page, 'r') as infile:
        html = infile.read()
        soup = BeautifulSoup(html, 'html.parser')

        prec_buttons = soup.find_all('input', {'value': 'Precinct Results'})

        for button in prec_buttons:
            oc_val = button['onclick']
            vals = oc_val.split('BuildPrecincts')[-1].split(';')[0].replace('(', '[').replace(')', ']').replace("'", '"')
            vals_list = [x for x in json.loads(vals) if x]
            endpoint = api_endpoint_fmt.format(*vals_list)
            filename = '-'.join(vals_list) + '.json'

            downloaded = download_data_file(endpoint, filename)

            print(f'Downloaded precinct data for {page} @ {downloaded}')

            time.sleep(random.uniform(1, 2))
