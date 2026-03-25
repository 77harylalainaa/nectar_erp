from django.shortcuts import render, redirect, get_object_or_404
from .models import Produit, Stock, MouvementStock, Categorie
from .forms import ProduitForm, StockForm, CategorieForm

def catalogue_produits(request):
    produits = Produit.objects.exclude(statut='archive')
    form = ProduitForm()
    categorie_form = CategorieForm()

    # ajout
    if request.method == 'POST':
        # produit
        if 'nom_produit' in request.POST:
            produit_id = request.POST.get('id_produit')
            if produit_id: #mode update
                produit = get_object_or_404(Produit, pk=produit_id)
                form = ProduitForm(request.POST, request.FILES, instance=produit)
            else: #mode create
                form = ProduitForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('catalogue_produits')
        # categorie
        elif 'nom' in request.POST:
            categorie_form = CategorieForm(request.POST)
            if categorie_form.is_valid():
                categorie_form.save()
                return redirect('catalogue_produits')

    return render(request, 'inventaire/catalogue.html', {
        'form': form,
        'categorie_form': categorie_form,
        'inventaire': produits
    })

def log_stocks(request):
    if request.method == "POST":
        produit_id = request.POST.get("produit_id")
        quantite = int(request.POST.get("quantite"))

        produit = get_object_or_404(Produit, pk=produit_id)

        stock, _ = Stock.objects.get_or_create(produit=produit)
        stock.quantite += quantite
        stock.save()

        MouvementStock.objects.create(
            produit=produit,
            type_mouvement='entree',
            quantite=quantite
        )

        return redirect('log_stocks')

    stocks = Stock.objects.select_related('produit')

    return render(request, 'inventaire/stock.html', {
        'stocks': stocks
    })

def archiver_produit(request, pk):
    if request.method == "POST":
        produit = get_object_or_404(Produit, pk=pk)
        produit.statut = 'archive'
        produit.save()
    return redirect('catalogue_produits')
def supprimer_produit(request, pk):
    if request.method == "POST":
        produit = get_object_or_404(Produit, pk=pk)
        produit.delete()
    return redirect('catalogue_produits')
