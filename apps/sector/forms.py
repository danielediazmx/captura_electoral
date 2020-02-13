from django import forms
from apps.sector.models import Sector


class SectorForm(forms.ModelForm):
    class Meta:
        model = Sector

        fields = {
            'nombre'
        }

        labels = {
            'nombre': 'Nombre'
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus'}),
        }
