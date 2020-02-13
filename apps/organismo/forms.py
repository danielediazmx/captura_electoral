from django import forms
from apps.organismo.models import Organismo


class OrganismoForm(forms.ModelForm):
    class Meta:
        model = Organismo

        fields = {
            'nombre'
        }

        labels = {
            'nombre': 'Nombre'
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'autofocus':'autofocus'}),
        }
