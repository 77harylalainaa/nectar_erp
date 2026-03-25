from django.urls import path
from . import views

urlpatterns = [
    path('clientslist/', views.liste_clients, name='liste_clients'),
    path('archiver-client/<int:pk>', views.archiver_client, name='archiver_client'),
    path('listproviders/', views.list_providers, name='list_providers'),
    path('archiver-fournisseur/<int:pk>', views.archiver_fournisseur, name='archiver_fournisseur'),
]