from django.urls import path
from apps.usuario.views import UserCreate, UserUpdate, destroyUsuario
from django_filters.views import FilterView
from captura_electoral.filters import filtroUsuario
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', login_required(FilterView.as_view(filterset_class=filtroUsuario, template_name='usuario/index.html')),
         name='usuario_index'),
    path('create', login_required(UserCreate.as_view()), name='usuario_crear'),
    path('edit/<int:pk>', login_required(UserUpdate.as_view()), name='usuario_editar'),
    path('delete/<int:id>', login_required(destroyUsuario), name='usuario_delete'),
]