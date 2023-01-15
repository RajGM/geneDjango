# import required packages

import factory
from random import randint
from random import choice
from django.test import TestCase
from django.conf import settings
from django.core.files import File
from .models import *

# model_factories holds the schema to test out the api endpoints

class ProteinFactory(factory.django.DjangoModelFactory):
    protein_id = "A0A016U701"
    taxa_id = 53326
    clade_identifier = "E"
    scientific_name = "Ancylostoma ceylanicum"
    domain_description = "Astacin(PeptidasefamilyM12A)"
    domain_id = "PF01400"
    domain_start = 1
    domain_stop = 83
    length_protein = 281

    class Meta:
        model = Protein

class DataSequencesFactory(factory.django.DjangoModelFactory):
    protein_id = "A0A016U701"
    protein_sequence = "MHELLHVIGLRHEHTRPERKDHIKIHWENIMEGFENQFALTSFDPDPYGIPYDYYSIMHYPKNASAKPGTITIETLDKKYQGVVRIAPEPHSQRLNGVASASPYCPSMDPYCKPSPSYTSLSTSPTLPSMPNTPTLPSMSSSTGQSPLSAEVTDEELQRISVRQLNQRLQGHDRQVVTMLKQKRRTLKNRGYALNCRVRRIQNQLQLEADNIQLRDQIRSLLQTLSDVQARLQYYEPTFMLHDYTYVSPTMPMTYHASTNLLAATTASNAVTSLCHMTQPQ"
    
    class Meta:
        model = DataSequences

class PfamDescriptionFactory(factory.django.DjangoModelFactory):
    pfam_id="PF01400"
    pfam_description="7transmembranereceptor(Secretinfamily)"

    class Meta:
        model = PfamDescription

