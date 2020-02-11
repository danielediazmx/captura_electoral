# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from apps.ubicacion.localidad.models import Localidad
from apps.ubicacion.localidad.forms import LocalidadForm
from django_filters.views import FilterView
from captura_electoral.filters import filtroLocalidad

# Create your views here.
class LocalidadIndex(FilterView):
    model = Localidad
    template_name = 'oficina/index.html'
    paginate_by = 15
    filterset_class = filtroLocalidad


class LocalidadCreate(CreateView):
    model = Localidad
    form_class = LocalidadForm
    template_name = 'oficina/form.html'
    success_url = reverse_lazy('oficina_index')


class LocalidadUpdate(UpdateView):
    model = Localidad
    form_class = LocalidadForm
    template_name = 'oficina/form.html'
    success_url = reverse_lazy('oficina_index')


def destroyLocalidad(request, id):
    localidad = Estado.objects.filter(pk=id).first()
    localidad.delete()
    return JsonResponse({'type': 'success'})