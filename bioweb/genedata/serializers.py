from rest_framework import serializers
from .models import *

# serializers.py is responsible for converting objects into data types understandable by javascript and front-end frameworks 

class ProteinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Protein
        fields = ['protein_id','taxa_id','clade_identifier','scientific_name','domain_description',
        'domain_id','domain_start','domain_stop','length_protein']

class PfamSerializer(serializers.ModelSerializer):
    class Meta:
        model = PfamDescription
        fields = ['pfam_id','pfam_description']

class DataSequencesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['protein_id','protein_sequence']
