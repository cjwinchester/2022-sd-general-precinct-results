import glob
import json
import csv


data_files = glob.glob('data/*.json')

csv_path = 'sd-general-election-2022-precinct-unofficial-results.csv'

headers = [
    'RaceID',
    'RaceName',
    'CandidateID',
    'calcCandidate',
    'calcCandidateVotes',
    'calcCandidatePercentage',
    'Winner',
    'CountyID',
    'CountyName',
    'PartyCode',
    'PartyName',
    'StatePrecinctID',
    'PrecinctName',
    'PrecinctsPartial',
    'PrecinctsReporting',
    'TotalPrecincts',
    'BallotOrder',
    'VoteFor',
    'RecountPercent',
    'RecountVotes'
]


with open(csv_path, 'w') as outfile:

    writer = csv.DictWriter(outfile, fieldnames=headers)

    writer.writeheader()

    for file in data_files:
        with open(file, 'r') as infile:
            data = json.load(infile)['d']
            for record in data:
                data_out = {hed: record[hed] for hed in headers}
                data_out['calcCandidate'] = ' '.join(data_out['calcCandidate'].split())
                writer.writerow(data_out)
            
