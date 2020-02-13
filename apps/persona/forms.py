from django import forms
from apps.persona.models import Persona
from apps.organismo.models import Organismo
from apps.sector.models import Sector
from apps.ubicacion.estado.models import Estado


class PersonaForm(forms.ModelForm):
    estado = forms.ModelChoiceField(queryset=Estado.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    sector = forms.ModelChoiceField(queryset=Sector.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    organismo = forms.ModelChoiceField(queryset=Organismo.objects.all(), widget=forms.Select(attrs={'class':'form-control'}))
    
    class Meta:
        model = Persona

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
            'sector',
            'organismo'
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
            'sector': 'Sector',
            'organismo': 'Organismo'
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidoPaterno': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidoMaterno': forms.TextInput(attrs={'class': 'form-control'}),
            'fechaNacimiento': forms.TextInput(attrs={'class': 'form-control'}),
            'curp': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'municipio': forms.Select(attrs={'class': 'form-control'}),
            'localidad': forms.Select(attrs={'class': 'form-control'}),
            'correo': forms.TextInput(attrs={'class': 'form-control', 'type': 'email'}),
            'facebook': forms.TextInput(attrs={'class': 'form-control'}),
            'whatsapp': forms.TextInput(attrs={'class': 'form-control'})
        }
