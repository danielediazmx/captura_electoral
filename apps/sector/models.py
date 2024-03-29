import os

from django.db import models


# Create your models here.

def renombrar(self, filename):
    nombre = self.nombre
    extension = os.path.splitext(filename)[1]
    if (extension):
        return 'logos/sector/{nombre}{ext}'.format(
            nombre=nombre,
            ext=extension)
    else:
        return 'logos/sector/default.jpg'


class Sector(models.Model):
    nombre = models.CharField(max_length=100)
    logo = models.ImageField(upload_to=renombrar, blank=True)

    def __str__(self):
        return self.nombre

    def __unicode__(self):
        return str(self.logo)

    def getRegistros(self):
        from apps.persona.models import Persona as Per
        personas = Per.objects.filter(sector_id=self.pk)
        return personas.count()
