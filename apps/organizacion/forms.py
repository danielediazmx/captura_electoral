from django import forms
from apps.organizacion.models import Organizacion


class OrganizacionForm(forms.ModelForm):
    class Meta:
        model = Organizacion

        fields = {
            'nombre'
        }

        labels = {
            'nombre': 'Nombre'
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }
