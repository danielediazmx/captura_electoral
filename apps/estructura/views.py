from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django_filters.views import FilterView
from apps.estructura.forms import EstructuraForm
from apps.estructura.models import Estructura
from captura_electoral.filters import filtroOrganismo

# Create your views here.

class index(FilterView):
    model = Estructura
    template_name = 'estructura/index.html'
    paginate_by = 15
    filterset_class = filtroOrganismo


class create(CreateView):
    model = Estructura
    form_class = EstructuraForm
    template_name = 'estructura/form.html'
    success_url = reverse_lazy('estructura_index')


class update(UpdateView):
    model = Estructura
    form_class = EstructuraForm
    template_name = 'estructura/form.html'
    success_url = reverse_lazy('estructura_index')


def destroy(request, id):
    estructura = Estructura.objects.filter(pk=id).first()
    estructura.delete()
    return JsonResponse({'type': 'success'})
