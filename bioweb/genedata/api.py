from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

#@api_view(['GET','POST'])
@api_view(['GET','POST'])
def protein_detail(request, pk):
    #query domain and add taxanomy as per format
    data = [{
      "taxaID": 568076,
      "domainStart": 157,
      "domainEnd": 314,
      "lengthProtein": 338,
      "proteinID": "A0A014PQC0",
      "cladeIdenitifier": "E",
      "scientificName": "Metarhizium robertsii",
      "domainDescription": "Glyceraldehyde 3-phosphate dehydrogenase catalytic domain",
      "domainID": "PF02800",
      "proteinSequence": "MVIGVGFLLVLFSSSVLGILNAGVQLRIEELFDTPGHTNNWAVLVCTSRFWFNYRHVSNVLALYHTVKRLGIPDSNIILMLAEDVPCNPRNPRPEAAVLSA"
    }]
    returnData = data[0]
    return Response(returnData)

@api_view(['GET'])
def pfam_detail(request, pk):
    
    data = [{
      "domain_id,": "PF00001,",
      "domain_description": "7transmembranereceptor(rhodopsinfamily)"
    },
    {
      "domain_id,": "PF00002,",
      "domain_description": "7transmembranereceptor(Secretinfamily)"
    }]
    returnData = data[0]
    return Response(returnData)

@api_view(['GET'])
def proteins_list(request, pk):
    #returns list of protein with matching taxa id with dbID and proteindID
    data = [{
        "id": 88766,
        "protein_id": "A0A091FY39"
    },
    {
        "id": 88761,
        "protein_id": "A0A091FMY9"
    },
    {
        "id": 88762,
        "protein_id": "A0A091FQA9"
    },
    {
        "id": 88763,
        "protein_id": "A0A091FRU1"
    }]

    return Response(data)

@api_view(['GET'])
def pfams_list(request, pk):
    #returns list of pfams with matching taxa id with domainID and domainDescription
    data = [{
        "id": 88896,
        "pfam_id": {
            "domain_id": "mobidb-lite",
            "domain_description": "disorder prediction"
        }
    },
    {
        "id": 88891,
        "pfam_id": {
            "domain_id": "PF00307",
            "domain_description": "Calponinhomology(CH)domain"
        }
    },
    {
        "id": 88892,
        "pfam_id": {
            "domain_id": "PF00415",
            "domain_description": "Regulatorofchromosomecondensation(RCC1)repeat"
        }
    },
    {
        "id": 88893,
        "pfam_id": {
            "domain_id": "PF07648",
            "domain_description": "Kazal-typeserineproteaseinhibitordomain"
        }
    }]

    return Response(data)

@api_view(['GET'])
def coverage(request, pk):
    #returns list of pfams with matching taxa id with domainID and domainDescription
    data = {
      "taxaID": 568076,
      "domainStart": 157,
      "domainEnd": 314,
      "lengthProtein": 338,
      "proteinID": "A0A014PQC0",
      "cladeIdenitifier": "E",
      "scientificName": "Metarhizium robertsii",
      "domainDescription": "Glyceraldehyde 3-phosphate dehydrogenase catalytic domain",
      "domainID": "PF02800",
      "proteinSequence": "MVIGVGFLLVLFSSSVLGILNAGVQLRIEELFDTPGHTNNWAVLVCTSRFWFNYRHVSNVLALYHTVKRLGIPDSNIILMLAEDVPCNPRNPRPEAAVLSA"
    }
    returnData = {"coverage":(data["domainStart"]-data["domainEnd"])/data["lengthProtein"]}
    return Response(returnData)

'''
@api_view(['GET'])
def genes_list(request):
    print("LOG HERE MORE")
    gene = Gene.objects.all()
    serializer = genes_list(gene, many=True)
    return Response(serializer.data)
'''

'''
    if request.method == 'POST':
        serializer = GeneSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''

'''
    try:
        gene = Gene.objects.get(pk=pk)
    except Gene.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        serializer = GeneSerializer(gene)
        return Response(serializer.data)
'''