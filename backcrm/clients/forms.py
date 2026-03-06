from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        exclude = ['ref_client']
        fields = '__all__'
        widgets = {
            'date_naissance_client': forms.DateInput(attrs={'type': 'date'})
        }