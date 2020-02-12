from django import forms
from apps.organizacion.models import Organizacion

class OrganizacionForm(forms.ModelForm):
    class Meta:
        model:Organizacion

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