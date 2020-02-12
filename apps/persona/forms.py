from django import forms
from apps.persona.models import Persona
from apps.organizacion.models import Organizacion
from apps.grupo.models import Grupo
from apps.ubicacion.estado.models import Estado


class PersonaForm(forms.ModelForm):
    class Meta:
        model: Persona

    fields = {
        'nombre'
        'apellidoPaterno'
        'apellidoMaterno'
        'fechaNacimiento'
        'curp'
        'direccion'
        'estado'
        'municipio'
        'localidad'
        'correo'
        'facebook'
        'whattsapp'
        'grupo'
        'organizacion'

    }

    labels = {
        'nombre': 'Nombre',
        'apellidoPaterno': 'Apellido Paterno',
        'apellidoMaterno': 'Apellido Materno',
        'fechaNacimiento': 'Fecha de Nacimiento',
        'curp': 'Curp',
        'direccion': 'Direccion',
        'estado': 'Estado',
        'municipio': 'Municipio',
        'localidad': 'Localidad',
        'correo': 'Correo',
        'facebook': 'Facebook',
        'whatsapp': 'Whatsapp',
        'grupo': 'Grupo',
        'organizacion': 'Organizacion'
    }

    widgets = {
        'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        'apellidoPaterno': forms.TextInput(attrs={'class': 'form-control'}),
        'apellidoMaterno': forms.TextInput(attrs={'class': 'form-control'}),
        'fechaNacimiento': forms.DateInput(attrs={'class': 'form-control'}),
        'curp': forms.TextInput(attrs={'class': 'form-control'}),
        'direccion': forms.TextInput(attrs={'class': 'form-control'}),
        'estado': forms.ModelChoiceField(queryset=Estado, attrs={'class': 'form-control'}),
        'municipio': forms.Select(attrs={'class': 'form-control'}),
        'localidad': forms.Select(attrs={'class': 'form-control'}),
        'correo': forms.EmailField(attrs={'class': 'form-control'}),
        'facebook': forms.TextInput(attrs={'class': 'form-control'}),
        'whattsapp': forms.TextInput(attrs={'class': 'form-control'}),
        'grupo': forms.ModelChoiceField(queryset=Grupo.objects.all(), attrs={'class': 'form-control'}),
        'organizacion': forms.ModelChoiceField(queryset=Organizacion.objects.all(), attrs={'class': 'form-control'})
    }
