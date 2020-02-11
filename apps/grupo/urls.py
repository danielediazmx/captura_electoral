from django.contrib.auth.decorators import login_required
from django.urls import path
from django_filters.views import FilterView
from apps.grupo.views import GrupoCreate, GrupoUpdate, destroyGrupo
from captura_electoral.filters import filtroGrupo

urlPatterns = [
    path('grupo/index',
         login_required(FilterView.as_view(filterset_class=filtroGrupo, template_name='grupo/index.html')),
         name='estado_index'),
    path('grupo/crear', login_required(GrupoCreate.as_view()), name='grupo_crear'),
    path('grupo/editar/<int:pk>', login_required(GrupoUpdate.as_view()), name='grupo_editar'),
    path('eliminar/<int:id_oficina>', login_required(destroyGrupo), name='grupo_eliminar'),

]