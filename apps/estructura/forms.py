from django import forms
from .models import Estructura


class EstructuraForm(forms.ModelForm):
    class Meta:
        model = Estructura

        fields = {
            'nombre'
        }

        labels = {
            'nombre': 'Nombre'
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'autofocus':'autofocus'}),
        }
