from django.urls import path
from . import views

urlpatterns = [
    path('catalogue/', views.catalogue_produits, name='catalogue_produits'),
    path('archiver-produit/<int:pk>', views.archiver_produit, name='archiver_produit'),
    path('supprimer-produit/<int:pk>', views.supprimer_produit, name='supprimer_produit'),
]