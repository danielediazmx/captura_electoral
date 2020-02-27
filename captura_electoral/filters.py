from django.contrib.auth.models import User
from django_filters import FilterSet, CharFilter, ModelChoiceFilter, DateFromToRangeFilter
from django_filters.widgets import RangeWidget
from django import forms
from apps.ubicacion.municipio.models import Municipio
from apps.sector.models import Sector
from apps.organismo.models import Organismo
from apps.estructura.models import Estructura
from apps.persona.models import Persona


class filtroUsuario(FilterSet):
    first_name = CharFilter(lookup_expr='icontains', label='Nombre',
                            widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = CharFilter(lookup_expr='icontains', label='Apellidos',
                           widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = CharFilter(lookup_expr='icontains', label='Correo',
                       widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']


class filtroPersona(FilterSet):
    sector = ModelChoiceFilter(queryset=Sector.objects.all(),
                               widget=forms.Select(attrs={'class': 'form-control'}))
    organismo = ModelChoiceFilter(queryset=Organismo.objects.all(),
                                  widget=forms.Select(attrs={'class': 'form-control'}))
    estructura = ModelChoiceFilter(queryset=Estructura.objects.all(),
                                   widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Persona
        fields = ['sector', 'organismo', 'estructura']


class filtroSector(FilterSet):
    nombre = CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Sector
        labels = {'nombre': 'Nombre'}
        fields = {'nombre'}


class filtroOrganismo(FilterSet):
    nombre = CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Organismo
        labels = {'nombre': 'Nombre'}
        fields = {'nombre'}


class filtroEstructura(FilterSet):
    nombre = CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Estructura
        labels = {'nombre': 'Nombre'}
        fields = {'nombre'}


class filtroMunicipio(FilterSet):
    clave = CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
    nombre = CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Municipio
        labels = {'clave': 'Clave', 'nombre': 'Nombre'}
        fields = {'clave', 'nombre'}
