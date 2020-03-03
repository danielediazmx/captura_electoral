from django import forms
from .models import Estructura


class EstructuraForm(forms.ModelForm):
    class Meta:
        model = Estructura

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
