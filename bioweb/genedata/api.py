from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET', 'POST'])
def protein_add(request):

    if request.method == 'POST':
        serializer = ProteinSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # query domain and add taxanomy as per format

    if request.method == 'GET':
        return Response()

# @api_view(['GET','POST'])
@api_view(['GET'])
def protein_detail(request, pk):

    print(pk)
    print("TEST STARTS")
    test = Protein.objects.filter(protein_id=pk)
    print(test)
    serializer = ProteinSerializer(test, many=True)
    print(serializer.data)
    print("TEST ENDS")
    return Response(serializer.data)

@api_view(['GET'])
def proteins_list(request, pk):
    # returns list of protein with matching taxa id with dbID and proteindID
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
    # returns list of pfams with matching taxa id with domainID and domainDescription
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
def pfam_detail(request, pk):

    try:
        pfam = PfamDescription.objects.get(pfam_id=pk)
    except PfamDescription.DoesNotExist:
       return Response({'Pfam':pk+' does not exists in database'})
    if request.method == 'GET':
        serializer = PfamSerializer(pfam)
        return Response(serializer.data)
    
@api_view(['GET'])
def coverage(request, pk):

    try:
        protein = Protein.objects.get(protein_id=pk)
    except Protein.DoesNotExist:
        return Response({'Protein':pk+' does not exists in database'})
    if request.method == 'GET':
        serializer = ProteinSerializer(protein)
        coverage = (serializer.data.get('domain_stop') - serializer.data.get('domain_start'))/serializer.data.get('length_protein')
        return Response({'coverage':coverage})