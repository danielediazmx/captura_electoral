from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from apps.persona.models import Persona
from apps.persona.forms import PersonaForm
from django_filters.views import FilterView
from captura_electoral.filters import filtroPersona
from django.contrib import messages


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


    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        userform = self.form_class(request.POST)
        if userform.is_valid():
            user = userform.save(commit=False)
            messages.add_message(request, messages.SUCCESS, 'Se ha guardado el registro con éxito')
            user.save()
            return redirect('/persona')
        else:
            print('errors hmmm',userform.errors)
            return render(request, 'persona/form.html', {'form': userform})



class PersonaUpdate(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'persona/form.html'
    success_url = reverse_lazy('persona_index')


def destroyPersona(request, id):
    persona = Persona.objects.filter(pk=id).first()
    persona.delete()
    return JsonResponse({'type': 'success'})