from django import forms
from apps.ubicacion.seccion.models import Seccion
from apps.ubicacion.seccion.models import Estado


class SeccionForm(forms.ModelForm):
    class Meta:
        model: Seccion

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
