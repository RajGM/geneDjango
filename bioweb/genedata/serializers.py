from rest_framework import serializers
from .models import *

'''
class GeneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gene
        fields = ['gene_id', 'entity', 'start', 'stop', 'sense', 'start_codon']

#@api_view(['GET'])

def genes_list(request):
    genes = models.Gene.objects.all()
    serializer = serializers.GeneSerializer(genes, many=True)
    return Response({
        'genes': serializer.data,
    })
'''
'''
class GeneSerializer(serializers.Serializer):
    gene_id = serializers.CharField(required=True, allow_blank=False, max_length=256)
    entity = serializers.CharField(required=True, allow_blank=False, max_length=256)
    start = serializers.IntegerField()
'''