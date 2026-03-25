from django import forms
from .models import Produit, Stock, Categorie

class CategorieForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['nom', 'parent']
class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        exclude = ['reference', 'statut']
        fields = '__all__'

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        exclude = ['dernier_maj']
        fields = '__all__'