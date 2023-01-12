from django.urls import path
from . import views
from . import api

urlpatterns = [
    path('', views.index, name='index'), #default page 
    path('api/protein/', api.protein_add), #POST path for protein
    path('api/protein/<str:pk>/', api.protein_detail), #GET path for protein
    path('api/pfam/<str:pk>/', api.pfam_detail), #GET path for pfam
    path('api/proteins/<int:pk>/', api.proteins_list), 
    path('api/pfams/<int:pk>/', api.pfams_list),
    path('api/coverage/<str:pk>/', api.coverage), #GET path for coverage
]