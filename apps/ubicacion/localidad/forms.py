from django import forms
from apps.ubicacion.localidad.models import Localidad
from apps.ubicacion.municipio.models import Municipio


class LocalidadForm(forms.ModelForm):
    class Meta:
        model: Localidad

    fields = {
        'clave'
        'nombre'
        'municipio'
    }

    labels = {
        'clave': 'Clave',
        'nombre': 'Nombre',
        'municipio': 'Municipio'
    }

    widgets = {
        'clave': forms.TextInput(attrs={'class': 'form-control'}),
        'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        'municipio': forms.ModelChoiceField(queryset=Municipio.objects.all(), empty_label='--Selecciona un Municipio--')
    }
