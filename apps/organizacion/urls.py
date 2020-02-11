from django.contrib.auth.decorators import login_required
from django.urls import path
from django_filters.views import FilterView
from apps.organizacion.views import OrganizacionCreate, OrganizacionUpdate, destroyOrganizacion
from captura_electoral.filters import filtroOrganizacion

urlPatterns = [
    path('organizacion/index',
         login_required(FilterView.as_view(filterset_class=filtroOrganizacion, template_name='organizacion/index.html')),
         name='organizacion_index'),
    path('organizacion/crear', login_required(OrganizacionCreate.as_view()), name='organizacion_crear'),
    path('organizacion/editar/<int:pk>', login_required(OrganizacionUpdate.as_view()), name='organizacion_editar'),
    path('eliminar/<int:id_oficina>', login_required(destroyOrganizacion), name='organizacion_eliminar'),

]