from django.db import models

# Create your models here.
class Estado(models.Model):
    clave = models.CharField(max_length=3)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return '{} {}'.format(self.clave, self.nombre)
