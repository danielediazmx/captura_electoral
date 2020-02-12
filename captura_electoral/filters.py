from django.contrib.auth.models import User
from django_filters import FilterSet, CharFilter, ModelChoiceFilter, DateFromToRangeFilter
from django_filters.widgets import RangeWidget
from django import forms
from apps.ubicacion.estado.models import Estado
from apps.ubicacion.municipio.models import Municipio
from apps.ubicacion.localidad.models import Localidad
from apps.ubicacion.seccion.models import Seccion
from apps.grupo.models import Grupo
from apps.organizacion.models import Organizacion

class filtroUsuario(FilterSet):
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
    class filtroPersona(FilterSet):
        nombre = CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
        apellidoPaterno = CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
        apellidoMaterno= CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
        curp = CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
        estado = ModelChoiceFilter(queryset=Estado.objects.all(),
                                      widget=forms.Select(attrs={'class': 'form-control'}))
        municipio = ModelChoiceFilter(queryset=Municipio.objects.all(),
                                   widget=forms.Select(attrs={'class': 'form-control'}))
        localidad = ModelChoiceFilter(queryset=Localidad.objects.all(),
                                   widget=forms.Select(attrs={'class': 'form-control'}))
        seccion = ModelChoiceFilter(queryset=Seccion.objects.all(),
                                   widget=forms.Select(attrs={'class': 'form-control'}))
        grupo = ModelChoiceFilter(queryset=Grupo.objects.all(),
                                   widget=forms.Select(attrs={'class': 'form-control'}))
        organizacion = ModelChoiceFilter(queryset=Organizacion.objects.all(),
                                   widget=forms.Select(attrs={'class': 'form-control'}))


class filtroGrupo(FilterSet):
        clave = CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
        nombre = CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))

        class Meta:
            model = Estado
            labels = {'clave': 'Clave', 'nombre': 'Nombre'}
            fields = {'clave', 'nombre'}

class filtroOrganizacion(FilterSet):
    class filtroOrganizacion(FilterSet):
        clave = CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
        nombre = CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))

        class Meta:
            model = Estado
            labels = {'clave': 'Clave', 'nombre': 'Nombre'}
            fields = {'clave', 'nombre'}

class filtroEstado(FilterSet):
    class filtroEstado(FilterSet):
        clave = CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
        nombre = CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))

        class Meta:
            model = Estado
            labels = {'clave': 'Clave', 'nombre': 'Nombre'}
            fields = {'clave', 'nombre'}

class filtroLocalidad(FilterSet):
    class filtroLocalidad(FilterSet):
        clave = CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
        nombre = CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))

        class Meta:
            model = Estado
            labels = {'clave': 'Clave', 'nombre': 'Nombre'}
            fields = {'clave', 'nombre'}

class filtroMunicipio(FilterSet):
    class filtroMunicipio(FilterSet):
        clave = CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
        nombre = CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))

        class Meta:
            model = Estado
            labels = {'clave': 'Clave', 'nombre': 'Nombre'}
            fields = {'clave', 'nombre'}

class filtroSeccion(FilterSet):
    class filtroSeccion(FilterSet):
        clave = CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))
        nombre = CharFilter(lookup_expr='icontains', widget=forms.TextInput(attrs={'class': 'form-control'}))

        class Meta:
            model = Estado
            labels = {'clave': 'Clave', 'nombre': 'Nombre'}
            fields = {'clave', 'nombre'}