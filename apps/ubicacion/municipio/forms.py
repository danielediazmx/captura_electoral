from django import forms
from apps.ubicacion.estado.models import Estado
from apps.ubicacion.municipio.models import Municipio


class MunicipioForm(forms.ModelForm):
    class Meta:
        model: Municipio

    fields = {
        'clave'
        'nombre'
        'estado'
    }

    labels = {
        'clave': 'Clave',
        'nombre': 'Nombre',
        'estado': 'Estado'
    }

    widgets = {
        'clave': forms.TextInput(attrs={'class': 'form-control'}),
        'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        'estado': forms.ModelChoiceField(queryset=Estado.objects.all(), empty_label='--Selecciona un Municipio--')
    }
