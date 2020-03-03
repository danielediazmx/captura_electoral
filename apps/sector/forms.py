from django import forms
from apps.sector.models import Sector


class SectorForm(forms.ModelForm):
    class Meta:
        model = Sector

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
            'logo': forms.TextInput(attrs={'class': 'form-control', 'type':'file'})
        }
