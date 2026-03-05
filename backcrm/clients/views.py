from django.shortcuts import render, redirect, get_object_or_404
from .models import Client

def liste_clients(request):
    clients = Client.objects.all()
    return render(request, 'clients/clients.html')
