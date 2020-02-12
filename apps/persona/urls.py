from django.contrib.auth.decorators import login_required
from django.urls import path
from django_filters.views import FilterView
from apps.persona.views import PersonaCreate, PersonaUpdate, destroyPersona
from captura_electoral.filters import filtroPersona

urlpatterns = [
    path('', FilterView.as_view(filterset_class=filtroPersona, template_name='persona/index.html'), name='persona_index'),
    path('create', PersonaCreate.as_view(), name='persona_create'),
    path('edit/<int:pk>', PersonaUpdate.as_view(), name='persona_edit'),
    path('delete/<int:id>', destroyPersona,name='persona_delete'),
]