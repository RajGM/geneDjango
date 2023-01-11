import os
import sys
import django
import csv
from collections import defaultdict

sys.path.append("/midTerm/bioweb")
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'bioweb.settings')
django.setup()

from genedata.models import *

data_file = '/midTerm/bioweb/pfam_descriptions.csv'
print("Data entry START")

pfams = list()
protein_sequences = list()
protein_details = list()

'''
with open(data_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = csv_reader.__next__()
    for row in csv_reader:
        pfams.append(row)


PfamDescription.objects.all().delete()

for pfam in pfams:
    indiRow = PfamDescription.objects.create(pfam_id=pfam[0],ogranism_scientific_name=pfam[1])
    indiRow.save()
'''

'''
data_file = '/midTerm/bioweb/protein_data_sequences.csv'

with open(data_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = csv_reader.__next__()
    for row in csv_reader:
        protein_sequences.append(row)

DataSequences.objects.all().delete()

for protein_seq in protein_sequences:
    indiSeq = DataSequences.objects.create(protein_id=protein_seq[0],protein_sequence=protein_seq[1])
    indiSeq.save()
'''

data_file = '/midTerm/bioweb/protein_detail.csv'
with open(data_file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    header = csv_reader.__next__()
    for row in csv_reader:
        protein_details.append(row)
        

Protein.objects.all().delete()

for proteinData in protein_details:
    indiProData = Protein.objects.create(protein_id=proteinData[0],taxa_id=proteinData[1],clade_identifier=proteinData[2],scientific_name=proteinData[3],domain_description=proteinData[4],domain_id=proteinData[5],domain_start=proteinData[6],domain_stop=proteinData[7],length_protein=proteinData[8])
    indiProData.save()

print("Data entry DONE")

