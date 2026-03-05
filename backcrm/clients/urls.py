from django.urls import path
from . import views

urlpatterns = [
    path('clientslist/', views.liste_clients, name='liste_clients'),
]