from django.shortcuts import render, redirect, get_object_or_404
from .models import Produit
from .forms import ProduitForm

def catalogue_produits(request):
    produits = Produit.objects.exclude(statut='archivé')
    form = ProduitForm()
    if request.method == 'POST':
        produit_id = request.POST.get('id_produit')
        if produit_id: #mode update
            produit = get_object_or_404(Produit, pk=produit_id)
            form = ProduitForm(request.POST, request.FILES, instance=produit)
        else: #mode create
            form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogue_produits')
        else:
            print(form.errors)

    return render(request, 'produits/catalogue.html', {
        'form': form,
        'produits': produits
    })

def archiver_produit(request, pk):
    if request.method == "POST":
        produit = get_object_or_404(Produit, pk=pk)
        produit.statut = 'archivé'
        produit.save()
    return redirect('catalogue_produits')
def supprimer_produit(request, pk):
    if request.method == "POST":
        produit = get_object_or_404(Produit, pk=pk)
        produit.delete()
    return redirect('catalogue_produits')
