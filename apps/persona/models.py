from django.db import models
from apps.estado.models import Estado
from apps.municipio.models import Municipio
from apps.grupo.models import Grupo
from apps.organizacion.models import Organizacion
from apps.localidad.models import Localidad


# Create your models here

class Persona(models.Model):
    nombre = models.CharField(max_length=150)
    apellidoPaterno = models.CharField(max_length=150)
    apellidoMaterno = models.CharField(max_length=150)
    fechaNacimiento = models.DateField
    curp = models.CharField(max_length=150)
    direccion = models.CharField(max_length=250)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)
    localidad=models.ForeignKey(Localidad, on_delete=models.CASCADE)
    correo=models.CharField(max_length=100)
    facebook = models.CharField(max_length=100)
    whattsapp = models.CharField(max_length=100)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE)
    organizacion = models.ForeignKey(Organizacion, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {} {}'.format(self.nombre, self.apellidoPaterno, self.apellidoMaterno)
