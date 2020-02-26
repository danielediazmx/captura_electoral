from django.db import models


# Create your models here.

class Municipio(models.Model):
    cp = models.CharField(max_length=10)
    nombre_asentamiento = models.CharField(max_length=200)
    tipo_asentamiento = models.CharField(max_length=200)
    municipio = models.CharField(max_length=100)
    estado = models.CharField(max_length=30)
    ciudad = models.CharField(max_length=100)
    tipo_zona = models.CharField(max_length=20)

    def __str__(self):
        return '{}'.format(self.municipio)
