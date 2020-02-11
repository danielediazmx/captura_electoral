from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from apps.ubicacion.seccion.models import Seccion
from apps.ubicacion.seccion.forms import SeccionForm
from django_filters.views import FilterView
from captura_electoral.filters import filtroSeccion


# Create your views here.

class SeccionIndex(FilterView):
    model = Seccion
    template_name = 'oficina/index.html'
    paginate_by = 15
    filterset_class = filtroSeccion


class SeccionCreate(CreateView):
    model = Seccion
    form_class = SeccionForm
    template_name = 'oficina/form.html'
    success_url = reverse_lazy('oficina_index')


class SeccionUpdate(UpdateView):
    model = Seccion
    form_class = SeccionForm
    template_name = 'oficina/form.html'
    success_url = reverse_lazy('oficina_index')


def destroySeccion(request, id):
    localidad = Seccion.objects.filter(pk=id).first()
    localidad.delete()
    return JsonResponse({'type': 'success'})