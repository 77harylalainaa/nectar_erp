from django.shortcuts import render
from produits.models import Produit
from clients.models import Client
from fournisseurs.models import Fournisseur

def the_archives(request):
    archives = []

    clients = Client.objects.filter(etat_client="archivé")
    for c in clients:
        archives.append({
            "type": "Client",
            "reference": c.ref_client,
            "id": c.id_client
        })

    produits = Produit.objects.filter(statut="archivé")
    for p in produits:
        archives.append({
            "type": "Produit",
            "reference": p.reference,
            "id": p.id_produit
        })

    fournisseurs = Fournisseur.objects.filter(activite_fournisseur="archivé")
    for f in fournisseurs:
        archives.append({
            "type": "Fournisseur",
            "reference": f.ref_fournisseur,
            "id": f.id_fournisseur
        })

    return render(request, 'archives/archives.html', {"archives": archives})
