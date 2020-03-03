from django.shortcuts import render
from apps.sector.models import Sector
from apps.organismo.models import Organismo
from apps.estructura.models import Estructura


# Create your views here.
def dashboardIndex(request):
    sectores = Sector.objects.all()
    organismos = Organismo.objects.all()
    estructuras = Estructura.objects.all()
    return render(request, 'dashboard/index.html',
                  {'sectores': sectores, 'organismos': organismos, 'estructuras': estructuras})
