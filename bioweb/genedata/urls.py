from django.urls import path
from . import views
from . import api

urlpatterns = [
    #path('', views.index.as_view(), name='index'),
    #path('', views.GeneList.as_view(), name='index'),
    path('api/protein/<str:pk>/', api.protein_detail), #GET adn POST both path
    path('api/pfam/<str:pk>/', api.pfam_detail), #GET path
    path('api/proteins/<int:pk>/', api.proteins_list),
    path('api/pfams/<int:pk>/', api.pfams_list),
    path('api/coverage/<str:pk>/', api.coverage),    
]