from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from apps.persona.models import Persona
from apps.persona.forms import PersonaForm
from django_filters.views import FilterView
from captura_electoral.filters import filtroPersona


class PersonaIndex(FilterView):
    model = Persona
    template_name = 'persona/index.html'
    paginate_by = 15
    filterset_class = filtroPersona


class PersonaCreate(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'persona/form.html'
    success_url = reverse_lazy('persona_index')


class PersonaUpdate(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'persona/form.html'
    success_url = reverse_lazy('persona_index')


def destroyPersona(request, id):
    persona = Persona.objects.filter(pk=id).first()
    persona.delete()
    return JsonResponse({'type': 'success'})