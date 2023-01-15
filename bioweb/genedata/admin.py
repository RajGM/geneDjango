#from django.contrib import admin
#from .models import *
# Register your models here.
# Register models here if we are supposed to perform CRUD operations from admin panel
# For this project, no such requirements 

from django.contrib import admin
from .models import *

class ProteinAdmin(admin.ModelAdmin):
    list_display = ['protein_id','taxa_id','clade_identifier','scientific_name','domain_description',
        'domain_id','domain_start','domain_stop','length_protein']

class PfamAdmin(admin.ModelAdmin):
    list_display = ['pfam_id','pfam_description']

class DataSequencesAdmin(admin.ModelAdmin):
    list_display = ['protein_id','protein_sequence']

admin.site.register(Protein,ProteinAdmin)
admin.site.register(PfamDescription,PfamAdmin)
admin.site.register(DataSequences,DataSequencesAdmin)