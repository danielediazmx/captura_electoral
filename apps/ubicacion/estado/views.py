from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from apps.ubicacion.estado.models import Estado
from apps.ubicacion.estado.forms import EstadoForm
from django_filters.views import FilterView
from captura_electoral.filters import filtroEstado

# Create your views here.
class EstadoIndex(FilterView):
    model = Estado
    template_name = 'oficina/index.html'
    paginate_by = 15
    filterset_class = filtroEstado


class EstadoCreate(CreateView):
    model = Estado
    form_class = EstadoForm
    template_name = 'oficina/form.html'
    success_url = reverse_lazy('oficina_index')


class EstadoUpdate(UpdateView):
    model = Estado
    form_class = EstadoForm
    template_name = 'oficina/form.html'
    success_url = reverse_lazy('oficina_index')


def destroyEstado(request, id_estado):
    estado = Estado.objects.filter(pk=id).first()
    estado.delete()
    return JsonResponse({'type': 'success'})
