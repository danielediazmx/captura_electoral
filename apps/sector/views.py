from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from apps.sector.models import Sector
from apps.sector.forms import SectorForm
from django_filters.views import FilterView
from captura_electoral.filters import filtroSector


# Create your views here.

class SectorIndex(FilterView):
    model = Sector
    template_name = 'sector/index.html'
    paginate_by = 15
    filterset_class = filtroSector


class SectorCreate(CreateView):
    model = Sector
    form_class = SectorForm
    template_name = 'sector/form.html'
    success_url = reverse_lazy('sector_index')


class SectorUpdate(UpdateView):
    model = Sector
    form_class = SectorForm
    template_name = 'sector/form.html'
    success_url = reverse_lazy('sector_index')


def destroySector(request, id):
    model = Sector.objects.filter(pk=id).first() or None
    if model:
        model.delete()
    return JsonResponse({'type': 'success'})
