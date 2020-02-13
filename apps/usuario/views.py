from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView
from django_filters.views import FilterView
from apps.usuario.forms import UserForm
from captura_electoral.filters import filtroUsuario
from django.contrib.auth.forms import UserCreationForm

class UserIndex(FilterView):
    model = User
    template_name = 'usuario/index.html'
    paginate_by = 15
    filterset_class = filtroUsuario


class UserCreate(CreateView):
    model = User
    form_class = UserForm
    template_name = 'usuario/form.html'
    success_url = reverse_lazy('usuario_index')

    def get_context_data(self, **kwargs):
        context = super(UserCreate, self).get_context_data(**kwargs)
        if 'userform' not in context:
            context['userform'] = self.form_class(self.request.GET)
        return context



class UserUpdate(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'usuario/form.html'
    success_url = reverse_lazy('usuario_index')

    def get_context_data(self, **kwargs):
        context = super(UserUpdate, self).get_context_data(**kwargs)
        if 'userform' not in context:
            context['userform'] = self.form_class(self.request.GET)
        return context
