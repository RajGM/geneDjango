# import required packages

import os
import sys
import django
import csv
from collections import defaultdict

# setting the required settings to run the populate script for the project
sys.path.append("/midTerm/bioweb")
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'bioweb.settings')
django.setup()

from genedata.models import *

# location of all of the datafiles
pfam_file = '/midTerm/bioweb/pfam_descriptions.csv'
proteinDetail_file = '/midTerm/bioweb/protein_detail.csv'
dataSeq_file = '/midTerm/bioweb/protein_data_sequences.csv'

# initilization of variables that will hold the data temporary until inserted into the database
pfams = list()
protein_sequences = list()
protein_details = list()

with open(pfam_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = csv_reader.__next__()
    for row in csv_reader:
        pfams.append(row)

with open(dataSeq_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = csv_reader.__next__()
    for row in csv_reader:
        protein_sequences.append(row)

with open(proteinDetail_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = csv_reader.__next__()
    for row in csv_reader:
        protein_details.append(row)

# deleting entries from the database to make it clean
PfamDescription.objects.all().delete()
DataSequences.objects.all().delete()
Protein.objects.all().delete()

# inseting data into database

for pfam in pfams:
    indiRow = PfamDescription.objects.create(pfam_id=pfam[0],pfam_description=pfam[1])
    indiRow.save()

for protein_seq in protein_sequences:
    indiSeq = DataSequences.objects.create(protein_id=protein_seq[0],protein_sequence=protein_seq[1])
    indiSeq.save()

for proteinData in protein_details:
    indiProData = Protein.objects.create(protein_id=proteinData[0],taxa_id=proteinData[1],clade_identifier=proteinData[2],scientific_name=proteinData[3],domain_description=proteinData[4],domain_id=proteinData[5],domain_start=proteinData[6],domain_stop=proteinData[7],length_protein=proteinData[8])
    indiProData.save()
