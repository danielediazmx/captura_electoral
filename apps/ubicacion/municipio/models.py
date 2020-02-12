from django.db import models
from apps.ubicacion.estado.models import Estado


# Create your models here.

class Municipio(models.Model):
    clave = models.CharField(max_length=3)
    nombre = models.CharField(max_length=150)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.clave, self.nombre)
