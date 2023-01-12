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
    returnlist = 'Protein does not exist for the given organismID:'+str(pk)
    proteinList = list((Protein.objects.filter(taxa_id=pk)).values_list('protein_id','pk'))
    
    if len(proteinList) == 0:
        Response(returnlist)
    else:
        returnlist = [] 
        for protein in proteinList:
            proteinobj = {
                "id":protein[1],
                "protein_id":protein[0]
            }
            returnlist.append(proteinobj)
    
    return Response(returnlist)
    

@api_view(['GET'])
def pfams_list(request, pk):
    #.values_list('protein_id','pk')
    returnlist = 'Protein does not exist for the given organismID:'+str(pk)
    domainList = list((Protein.objects.filter(taxa_id=pk)).values('domain_id'))
    print(domainList)
    if(len(domainList)==0):
        Response(returnlist)
    else:
        returnlist = []
        for domain in domainList:
            print(domain["domain_id"])
            domainData=list(PfamDescription.objects.filter(pfam_id=domain["domain_id"]).values_list('pk','ogranism_scientific_name'))
            print(domainData)
            pfamObj = {
                "id":domainData[0][0],
                "pfam_id":{
                    "domain_id":domain["domain_id"],
                    "domain_description":domainData[0][1]
                }
            }
            returnlist.append(pfamObj)
        
    return Response(returnlist)

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