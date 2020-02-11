from django import forms
from apps.grupo.models import Grupo


class GrupoForm(forms.ModelForm):
    class Meta:
        model: Grupo

    fields = {
        'clave'
        'nombre'
    }

    labels = {
        'clave': 'Clave',
        'nombre': 'Nombre'
    }

    widgets = {
        'clave': forms.TextInput(attrs={'class': 'form-control'}),
        'nombre': forms.TextInput(attrs={'class': 'form-control'}),
    }
