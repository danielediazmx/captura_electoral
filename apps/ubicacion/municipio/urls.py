from django.contrib.auth.decorators import login_required
from django.urls import path
from django_filters.views import FilterView
from apps.ubicacion.municipio.views import MunicipioCreate, MunicipioUpdate
from captura_electoral.filters import filtroMunicipio

urlPatterns = [
    path('municipio/index',
         login_required(FilterView.as_view(filterset_class=filtroMunicipio, template_name='ubicacion/municipio/index.html')),
         name='municipio_index'),
    path('municipio/crear', login_required(MunicipioCreate.as_view()), name='municipio_crear'),
    path('municipio/editar/<int:pk>', login_required(MunicipioUpdate.as_view()), name='municipio_editar'),
]