from django.db import models


# Create your models here.

class Estructura(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return '{}'.format(self.nombre)

    def getRegistros(self):
        from apps.persona.models import Persona as Per
        personas = Per.objects.filter(estructura_id=self.pk)
        return personas.count()
