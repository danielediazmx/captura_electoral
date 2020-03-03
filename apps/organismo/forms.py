from django import forms
from apps.organismo.models import Organismo


class OrganismoForm(forms.ModelForm):
    class Meta:
        model = Organismo

        fields = {
            'nombre',
            'logo'
        }

        labels = {
            'nombre': 'Nombre',
            'logo': 'Logo'
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus'}),
            'logo': forms.FileInput(attrs={'class': 'form-control', 'type':'file'})
        }
