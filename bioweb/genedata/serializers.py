from rest_framework import serializers
from .models import *

class ProteinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Protein
        fields = ['protein_id','taxa_id','clade_identifier','scientific_name','domain_description',
        'domain_id','domain_start','domain_stop','length_protein']

class PfamSerializer(serializers.ModelSerializer):
    class Meta:
        model = PfamDescription
        fields = ['pfam_id','ogranism_scientific_name']

class DataSequencesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['protein_id','protein_sequence']
