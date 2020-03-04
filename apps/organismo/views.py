from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from apps.organismo.models import Organismo
from apps.organismo.forms import OrganismoForm
from django_filters.views import FilterView
from captura_electoral.filters import filtroOrganismo


# Create your views here.

class OrganismoIndex(FilterView):
    model = Organismo
    template_name = 'organismo/index.html'
    paginate_by = 15
    filterset_class = filtroOrganismo


class OrganismoCreate(CreateView):
    model = Organismo
    form_class = OrganismoForm
    template_name = 'organismo/form.html'
    success_url = reverse_lazy('organismo_index')


class OrganismoUpdate(UpdateView):
    model = Organismo
    form_class = OrganismoForm
    template_name = 'organismo/form.html'
    success_url = reverse_lazy('organismo_index')


def destroyOrganismo(request, id):
    organismo = Organismo.objects.filter(pk=id).first()
    organismo.delete()
    return JsonResponse({'type': 'success'})
