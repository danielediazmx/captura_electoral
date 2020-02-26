from django.db import models
from apps.ubicacion.municipio.models import Municipio
from apps.sector.models import Sector
from apps.organismo.models import Organismo
from apps.estructura.models import Estructura


# Create your models here

class Persona(models.Model):
    sexo = ((1, 'Masculino'), (2, 'Femenino'))
    nombre = models.CharField(max_length=100)
    apellidoPaterno = models.CharField(max_length=100, blank=True, null=True, default='')
    apellidoMaterno = models.CharField(max_length=100, blank=True, null=True, default='')
    sexo = models.IntegerField(choices=sexo, default=1)
    fechaNacimiento = models.DateField(blank=True, null=True, default=None)
    # curp = models.CharField(max_length=150)
    clave_electoral = models.CharField(max_length=30, blank=True, null=True, default='')
    direccion = models.CharField(max_length=250, blank=True, null=True, default='')
    calle = models.CharField(max_length=100, blank=True, null=True, default='')
    numero = models.CharField(max_length=100, null=True, blank=True, default='')
    colonia = models.CharField(max_length=100, null=True, blank=True, default='')
    # estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE, blank=True, null=True, default=None)
    municipio_text = models.CharField(max_length=100, blank=True, null=True, default='')
    # localidad = models.ForeignKey(Localidad, on_delete=models.CASCADE)
    # seccion = models.ForeignKey(Seccion, on_delete=models.CASCADE, blank=True, null=True)
    correo = models.EmailField(max_length=100, null=True, blank=True, default='')
    facebook = models.CharField(max_length=100, null=True, blank=True, default='')
    whatsapp = models.CharField(max_length=100, null=True, blank=True, default='')
    twitter = models.CharField(max_length=100, null=True, blank=True, default='')
    instagram = models.CharField(max_length=100, null=True, blank=True, default='')
    sector = models.ForeignKey(Sector, on_delete=models.CASCADE, default=None, blank=True, null=True)
    organismo = models.ForeignKey(Organismo, on_delete=models.CASCADE, default=None, blank=True, null=True)
    estructura = models.ForeignKey(Estructura, on_delete=models.CASCADE, default=None, blank=True, null=True)
    nivel_confianza = models.IntegerField(default=0)
    nota = models.CharField(max_length=500, null=True, blank=True, default='')
    seccion_electoral = models.CharField(max_length=10, blank=True, null=True, default='')

    def __str__(self):
        return '{} {} {}'.format(self.nombre, self.apellidoPaterno, self.apellidoMaterno)
