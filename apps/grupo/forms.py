from django import forms
from apps.grupo.models import Grupo


class GrupoForm(forms.ModelForm):
    class Meta:
        model = Grupo

        fields = {
            'nombre'
        }

        labels = {
            'nombre': 'Nombre'
        }

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }
