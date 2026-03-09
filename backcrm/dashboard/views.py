from django.shortcuts import render
from produits.models import Produit
from clients.models import Client

def dashboard_home(request):
    produits = Produit.objects.count()
    clients = Client.objects.count()
    return render(request, 'dashboard/dashboard.html', {
        'produits': produits,'clients': clients
    })
