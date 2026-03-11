from django import forms
from .models import Fournisseur

class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        exclude = ['ref_fournisseur', 'activite_fournisseur']
        fields = '__all__'