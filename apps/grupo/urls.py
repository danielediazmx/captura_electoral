from django.contrib.auth.decorators import login_required
from django.urls import path
from django_filters.views import FilterView
from apps.grupo.views import GrupoCreate, GrupoUpdate, destroyGrupo, GrupoIndex

urlpatterns = [
    path('',GrupoIndex.as_view(), name='grupo_index'),
    path('create', GrupoCreate.as_view(), name='grupo_crear'),
    path('edit/<int:pk>', GrupoUpdate.as_view(), name='grupo_editar'),
    path('delete/<int:id>', destroyGrupo, name='grupo_eliminar'),

]