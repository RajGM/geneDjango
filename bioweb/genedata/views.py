from django.shortcuts import render
from .models import *

# views.py contains the html page/template to render/send to client based on request

def index(request):
    return render(request,'genedata/index.html',{"test":"Test"})

