from django.contrib.auth.decorators import login_required
from django.urls import path
from django_filters.views import FilterView
from apps.ubicacion.seccion.views import SeccionCreate, SeccionUpdate
from captura_electoral.filters import filtroSeccion

urlPatterns = [
    path('seccion/index',
         login_required(FilterView.as_view(filterset_class=filtroSeccion, template_name='ubicacion/seccion/index.html')),
         name='estado_index'),
    path('seccion/crear', login_required(SeccionCreate.as_view()), name='estado_crear'),
    path('seccion/editar/<int:pk>', login_required(SeccionUpdate.as_view()), name='oficina_editar'),
]