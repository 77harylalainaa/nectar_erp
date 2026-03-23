from django.shortcuts import render, redirect, get_object_or_404
from .models import Fournisseur, Client
from .forms import FournisseurForm, ClientForm

def liste_clients(request):
    clients = Client.objects.exclude(etat_client='archivé')
    form = ClientForm()
    if request.method == 'POST':
        client_id = request.POST.get('id_client')
        if client_id: #update
            client = get_object_or_404(Client, pk=client_id)
            form = ClientForm(request.POST, request.FILES, instance=client)
        else: #create
            form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('liste_clients')
        else:
            print(form.errors)

    return render(request, 'clients/clients.html', {
        'form': form,
        'clients': clients
    })

def archiver_client(request, pk):
    if request.method == "POST":
        client = get_object_or_404(Client, pk=pk)
        client.etat_client = 'archivé'
        client.save()
    return redirect('liste_clients')

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
