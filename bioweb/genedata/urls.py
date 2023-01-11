from django.urls import path
from . import views
from . import api

urlpatterns = [
    path('', views.GeneList.as_view(), name='index'),
    path('api/gene/<int:pk>/', api.gene_detail),
    #POST ADD path('api/protein/<int:pk>/', api.gene_detail),
    #GET path('api/protein/<int:pk>/', api.gene_detail),
    #path('api/proteins/<int:pk>/', api.gene_detail),
    #pfamID path('api/pfam/<int:pk>/', api.gene_detail),
    #TaxaID path('api/pfams/<int:pk>/', api.gene_detail),
    #GET proteinID path('api/coverage/<int:pk>/', api.gene_detail),    
]