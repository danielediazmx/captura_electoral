from django.db import models
from apps.ubicacion.estado.models import Estado
from apps.ubicacion.municipio.models import Municipio
from apps.sector.models import Sector
from apps.organismo.models import Organismo
from apps.ubicacion.localidad.models import Localidad
from apps.ubicacion.seccion.models import Seccion


# Create your models here

class Persona(models.Model):
    nombre = models.CharField(max_length=100)
    apellidoPaterno = models.CharField(max_length=100)
    apellidoMaterno = models.CharField(max_length=100)
    fechaNacimiento = models.DateField(null=False)
    curp = models.CharField(max_length=150)
    clave_electoral = models.CharField(max_length=30, default=00000000)
    direccion = models.CharField(max_length=250)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)
    seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE, blank=True, null=True)
    correo = models.EmailField(max_length=100)
    facebook = models.CharField(max_length=100, null=True)
    whatsapp = models.CharField(max_length=100, null=True)
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE)
    organismo = models.ForeignKey(Organismo, on_delete=models.CASCADE)
    nivel_confianza = models.IntegerField(default=0)

    def __str__(self):
        return '{} {} {}'.format(self.nombre, self.apellidoPaterno, self.apellidoMaterno)
