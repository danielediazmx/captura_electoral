from django import forms
from apps.persona.models import Persona
from apps.organizacion.models import Organizacion
from apps.grupo.models import Grupo
from apps.ubicacion.estado.models import Estado


class PersonaForm(forms.ModelForm):
    class Meta:
        model = Persona
        estado = forms.ModelChoiceField(queryset=Estado.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
        grupo = forms.ModelChoiceField(queryset=Grupo.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
        organizacion = forms.ModelChoiceField(queryset=Organizacion.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))

        fields = [
            'nombre',
            'apellidoPaterno',
            'apellidoMaterno',
            'fechaNacimiento',
            'curp',
            'direccion',
            'estado',
            'municipio',
            'localidad',
            'correo',
            'facebook',
            'whatsapp',
            'grupo',
            'organizacion'
        ]

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
            'municipio': forms.Select(attrs={'class': 'form-control'}),
            'localidad': forms.Select(attrs={'class': 'form-control'}),
            'correo': forms.TextInput(attrs={'class': 'form-control', 'type': 'email'}),
            'facebook': forms.TextInput(attrs={'class': 'form-control'}),
            'whattsapp': forms.TextInput(attrs={'class': 'form-control'})
        }
