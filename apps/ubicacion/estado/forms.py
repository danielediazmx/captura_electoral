from django import forms
from apps.ubicacion.estado.models import Estado


class EstadoForm(forms.ModelForm):
    class Meta:
        model: Estado

    fields = [
        'clave'
        'nombre'
    ]

    labels = {
        'clave': 'Clave',
        'nombre': 'Nombre'
    }

    widgets = {
        'clave': forms.TextInput(attrs={'class': 'form-control'}),
        'nombre': forms.TextInput(attrs={'class': 'form-control'})
    }
