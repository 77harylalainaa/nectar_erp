from django import forms
from .models import Produit

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        exclude = ['reference', 'statut']
        fields = '__all__'