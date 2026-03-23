from django.shortcuts import render
from produits.models import Produit
from nectarcrm.models import Client, Fournisseur

def dashboard_home(request):
    produits = Produit.objects.count()
    clients = Client.objects.count()
    fournisseurs = Fournisseur.objects.count()
    return render(request, 'dashboard/dashboard.html', {
        'produits': produits,
        'clients': clients,
        'fournisseurs': fournisseurs,
    })
