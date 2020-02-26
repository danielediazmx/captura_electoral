from django.contrib.auth.decorators import login_required
from django.urls import path
from django_filters.views import FilterView
from apps.persona.views import PersonaCreate, PersonaUpdate, destroyPersona, PersonaIndex
from captura_electoral.filters import filtroPersona

urlpatterns = [
    path('', login_required(PersonaIndex.as_view()), name='persona_index'),
    path('create', login_required(PersonaCreate.as_view()), name='persona_create'),
    path('edit/<int:pk>', login_required(PersonaUpdate.as_view()), name='persona_edit'),
    path('delete/<int:id>', login_required(destroyPersona),name='persona_delete'),
]