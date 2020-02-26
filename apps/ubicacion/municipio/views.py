from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from apps.ubicacion.municipio.models import Municipio
from apps.ubicacion.municipio.forms import MunicipioForm
from django_filters.views import FilterView
from captura_electoral.filters import filtroMunicipio
from django.core import serializers


# Create your views here.

class MunicipioIndex(FilterView):
    model = Municipio
    template_name = 'oficina/index.html'
    paginate_by = 15
    filterset_class = filtroMunicipio


class MunicipioCreate(CreateView):
    model = Municipio
    form_class = MunicipioForm
    template_name = 'oficina/form.html'
    success_url = reverse_lazy('oficina_index')


class MunicipioUpdate(UpdateView):
    model = Municipio
    form_class = MunicipioForm
    template_name = 'oficina/form.html'
    success_url = reverse_lazy('oficina_index')


def destroyMunicipio(request, id):
    localidad = Municipio.objects.filter(pk=id).first()
    localidad.delete()
    return JsonResponse({'type': 'success'})


def GetMunicipioByZip(request):
    zipCode = request.GET.get('zipCode')
    municipios = Municipio.objects.filter(cp=zipCode).all() or []
    response_data = serializers.serialize('json', municipios)
    return HttpResponse(response_data, content_type='application/json')