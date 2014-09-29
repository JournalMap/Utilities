# pubmed2doi.py
# script for calling a web service for converting PubMed ID numbers to DOIs

import os
import requests
import csv

os.chdir('/Users/jasokarl/Dropbox/JournalMap/Journal_Map_Data/west_nile_virus')
test = os.getcwd()

## inputs
infile = 'pmids.csv'
outfile = 'dois.csv'

## setup the output file
o = open(outfile, 'wb')
writer = csv.writer(o)
writer.writerow(["pmid","doi"])

## crack the csv and start iteration
with open(infile, 'rb') as f:
    reader = csv.reader(f.read().splitlines())
    for row in reader:
        pmid = str(row[0])
        print pmid
        response = requests.get('http://www.pmid2doi.org/rest/json/doi/'+pmid)
        if response.status_code == 404:
            doi = ''
        else:
            data = response.json()
            doi = data['doi']
        print doi
        writer.writerow([pmid,doi])

o.close
f.close