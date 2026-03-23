import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from produits.models import Produit
from nectarcrm.models import Client, Fournisseur

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

def restore_item(request):
    if request.method == "POST":
        data = json.loads(request.body)

        item_id = data.get("id")
        item_type = data.get("type")

        try:
            if item_type == "client":
                obj = Client.objects.get(id_client=item_id)
                obj.etat_client = "inactif"

            elif item_type == "produit":
                obj = Produit.objects.get(id_produit=item_id)
                obj.statut = "non_disponible"

            elif item_type == "fournisseur":
                obj = Fournisseur.objects.get(id_fournisseur=item_id)
                obj.activite_fournisseur = "inactif"

            else:
                return JsonResponse({"success": False, "error": "Type invalide"})

            obj.save()
            return JsonResponse({"success": True})

        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})