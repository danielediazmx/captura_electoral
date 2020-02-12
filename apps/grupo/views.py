from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from apps.grupo.models import Grupo
from apps.grupo.forms import GrupoForm
from django_filters.views import FilterView
from captura_electoral.filters import filtroGrupo


# Create your views here.

class GrupoIndex(FilterView):
    model = Grupo
    template_name = 'grupo/index.html'
    paginate_by = 15
    filterset_class = filtroGrupo


class GrupoCreate(CreateView):
    model = Grupo
    form_class = GrupoForm
    template_name = 'oficina/form.html'
    success_url = reverse_lazy('oficina_index')


class GrupoUpdate(UpdateView):
    model = Grupo
    form_class = GrupoForm
    template_name = 'oficina/form.html'
    success_url = reverse_lazy('oficina_index')


def destroyGrupo(request, id):
    localidad = Grupo.objects.filter(pk=id).first()
    localidad.delete()
    return JsonResponse({'type': 'success'})
