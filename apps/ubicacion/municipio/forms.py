from django import forms
# from apps.ubicacion.estado.models import Estado
from apps.ubicacion.municipio.models import Municipio


class MunicipioForm(forms.ModelForm):
    class Meta:
        model: Municipio

    fields = {
    }

    labels = {
    }

    widgets = {
    }
