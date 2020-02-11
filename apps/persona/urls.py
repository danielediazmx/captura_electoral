from django.contrib.auth.decorators import login_required
from django.urls import path
from django_filters.views import FilterView
from apps.persona.views import PersonaCreate, PersonaUpdate, destroyPersona
from captura_electoral.filters import filtroPersona

urlPatterns = [
    path('persona/index',
         login_required(FilterView.as_view(filterset_class=filtroPersona, template_name='persona/index.html')),
         name='persona_index'),
    path('persona/crear', login_required(PersonaCreate.as_view()), name='persona_crear'),
    path('persona/editar/<int:pk>', login_required(PersonaUpdate.as_view()), name='persona_editar'),
    path('eliminar/<int:id>', login_required(destroyPersona),name='persona_eliminar'),
]