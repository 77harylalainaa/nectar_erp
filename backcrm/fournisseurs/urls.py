from django.urls import path
from . import views

urlpatterns = [
    path('listproviders/', views.list_providers, name='list_providers'),
    path('archiver-fournisseur/<int:pk>', views.archiver_fournisseur, name='archiver_fournisseur'),
]