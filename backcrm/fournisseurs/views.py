from django.shortcuts import render, redirect, get_object_or_404
from .models import Fournisseur
from .forms import FournisseurForm

def list_providers(request):
    fournisseurs = Fournisseur.objects.exclude(activite_fournisseur='archivé')
    form = FournisseurForm()
    if request.method == 'POST':
        fournisseur_id = request.POST.get('id_fournisseur')
        if fournisseur_id: #mise à jour
            fournisseur = get_object_or_404(Fournisseur, pk=fournisseur_id)
            form = FournisseurForm(request.POST, request.FILES, instance=fournisseur)
        else: #ajout
            form = FournisseurForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_providers')
        else:
            print(form.errors)

    return render(request, 'fournisseurs/providers.html', {
        'form': form,
        'fournisseurs': fournisseurs
    })
def archiver_fournisseur(request, pk):
    if request.method == "POST":
        fournisseur = get_object_or_404(Fournisseur, pk=pk)
        fournisseur.activite_fournisseur = 'archivé'
        fournisseur.save()
    return redirect('list_providers')
