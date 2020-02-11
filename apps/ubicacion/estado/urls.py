from django.contrib.auth.decorators import login_required
from django.urls import path
from django_filters.views import FilterView
from apps.ubicacion.estado.views import EstadoIndex, EstadoCreate, EstadoUpdate
from captura_electoral.filters import filtroEstado

urlPatterns = [
    path('estado/index',
         login_required(FilterView.as_view(filterset_class=filtroEstado, template_name='ubicacion/estado/index.html')),
         name='estado_index'),
    path('estado/crear', login_required(EstadoCreate.as_view()), name='estado_crear'),
    path('estado/editar/<int:pk>', login_required(EstadoUpdate.as_view()), name='estado_editar'),
]
