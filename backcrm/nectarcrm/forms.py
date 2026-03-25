from django import forms
from .models import Fournisseur, Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        exclude = ['ref', 'statut']
        fields = '__all__'
        widgets = {
            'date_naissance_client': forms.DateInput(attrs={'type': 'date'})
        }

class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        exclude = ['ref', 'statut']
        fields = '__all__'