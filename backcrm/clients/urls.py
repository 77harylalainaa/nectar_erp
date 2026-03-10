from django.urls import path
from . import views

urlpatterns = [
    path('clientslist/', views.liste_clients, name='liste_clients'),
    path('archiver-client/<int:pk>', views.archiver_client, name='archiver_client'),
]