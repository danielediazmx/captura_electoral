from django.urls import path
from apps.usuario.views import UserCreate, UserUpdate
from django_filters.views import FilterView
from captura_electoral.filters import filtroUsuario
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', FilterView.as_view(filterset_class=filtroUsuario, template_name='usuario/index.html'),
         name='usuario_index'),
    path('create', UserCreate.as_view(), name='usuario_crear'),
    path('edit/<int:pk>', UserUpdate.as_view(), name='usuario_editar')
]