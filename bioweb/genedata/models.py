from django.db import models
# Create your models here.
class DataSequences(models.Model):
    protein_id = models.CharField(max_length=256, null=False,
    blank=False, db_index=True)
    protein_sequence = models.CharField(max_length=40000, null=False,blank=False)
    
    def __str__(self):
        return self.protein_id

class Protein(models.Model):
    protein_id = models.CharField(max_length=20, null=False,
    blank=False, db_index=True)
    taxa_id = models.IntegerField(null=False,
    blank=False, db_index=True)
    clade_identifier = models.CharField(max_length=1,default="E")
    scientific_name = models.CharField(max_length=256)
    domain_description = models.CharField(max_length=256, null=False, blank=False)
    domain_id = models.CharField(max_length=20, null=False,
    blank=False, db_index=True)
    domain_start = models.IntegerField(null=False, blank=True)
    domain_stop = models.IntegerField(null=False, blank=True)
    length_protein = models.IntegerField(null=False, blank=True)
    
    def __str__(self):
        return self.protein_id

class PfamDescription(models.Model):
    pfam_id = models.CharField(max_length=20, null=False,
    blank=False, db_index=True)
    ogranism_scientific_name = models.CharField(max_length=256)

    def __str__(self):
        return self.pfam_id