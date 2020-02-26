from django.contrib.auth.decorators import login_required
from django.urls import path
from django_filters.views import FilterView
from apps.ubicacion.municipio.views import GetMunicipioByZip

urlpatterns = [
    path('get-by-zip/',
         login_required(GetMunicipioByZip),
         name='municipio_get_by_zip')
]