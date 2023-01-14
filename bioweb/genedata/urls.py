from django.urls import path
from . import views
from . import api

# url patterns maps api-end point with the supposed function to call
urlpatterns = [
    path('', views.index, name='index'), #default page 
    path('api/protein/', api.protein_add, name="portein_add"), #POST path for protein
    path('api/protein/<str:pk>/', api.protein_detail, name="protein_get"), #GET path for protein
    path('api/pfam/<str:pk>/', api.pfam_detail, name="pfam_get"), #GET path for pfam
    path('api/proteins/<int:pk>/', api.proteins_list, name="proteins_get"), 
    path('api/pfams/<int:pk>/', api.pfams_list, name="pfams_get" ),
    path('api/coverage/<str:pk>/', api.coverage, name="coverage_get"), #GET path for coverage
]