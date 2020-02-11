from django.db import models
from apps.municipio.models import Municipio


# Create your models here.

class Localidad(models.Model):
    clave = models.CharField(max_length=5)
    nombre = models.CharField(max_length=100)
    municipio = models.ForeignKey(Municipio, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.clave, self.nombre)
