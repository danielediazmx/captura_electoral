from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from apps.organizacion.models import Organizacion
from apps.organizacion.forms import OrganizacionForm
from django_filters.views import FilterView
from captura_electoral.filters import filtroOrganizacion


# Create your views here.

class OrganizacionIndex(FilterView):
    model = Organizacion
    template_name = 'organizacion/index.html'
    paginate_by = 15
    filterset_class = filtroOrganizacion


class OrganizacionCreate(CreateView):
    model = Organizacion
    form_class = OrganizacionForm
    template_name = 'organizacion/form.html'
    success_url = reverse_lazy('organizacion_index')


class OrganizacionUpdate(UpdateView):
    model = Organizacion
    form_class = OrganizacionForm
    template_name = 'organizacion/form.html'
    success_url = reverse_lazy('organizacion_index')


def destroyOrganizacion(request, id):
    organizacion = Organizacion.objects.filter(pk=id).first()
    organizacion.delete()
    return JsonResponse({'type': 'success'})