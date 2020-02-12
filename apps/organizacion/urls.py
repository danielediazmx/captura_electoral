from django.contrib.auth.decorators import login_required
from django.urls import path
from django_filters.views import FilterView
from apps.organizacion.views import OrganizacionCreate, OrganizacionUpdate, destroyOrganizacion
from captura_electoral.filters import filtroOrganizacion

urlpatterns = [
    path('',
         FilterView.as_view(filterset_class=filtroOrganizacion, template_name='organizacion/index.html'),
         name='organizacion_index'),
    path('create', OrganizacionCreate.as_view(), name='organizacion_crear'),
    path('edit/<int:pk>', OrganizacionUpdate.as_view(), name='organizacion_editar'),
    path('delete/<int:id>', destroyOrganizacion, name='organizacion_eliminar'),

]