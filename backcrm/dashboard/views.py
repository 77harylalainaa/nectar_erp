from django.shortcuts import render
from produits.models import Produit

def dashboard_home(request):
    produits = Produit.objects.count()
    return render(request, 'dashboard/dashboard.html', {'produits': produits})
