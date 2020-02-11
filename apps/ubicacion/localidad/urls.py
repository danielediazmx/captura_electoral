from django.contrib.auth.decorators import login_required
from django.urls import path
from django_filters.views import FilterView
from apps.ubicacion.localidad.views import LocalidadCreate, LocalidadUpdate
from captura_electoral.filters import filtroLocalidad

urlPatterns = [
    path('localidad/index',
         login_required(FilterView.as_view(filterset_class=filtroLocalidad, template_name='ubicacion/localidad/index.html')),
         name='localidad_index'),
    path('localidad/crear', login_required(LocalidadCreate.as_view()), name='localidad_crear'),
    path('localidad/editar/<int:pk>', login_required(LocalidadUpdate.as_view()), name='localidad_editar'),
]