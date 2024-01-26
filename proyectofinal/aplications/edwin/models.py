from django.db import models

# Create your models here.
class BDInmueble(models.Model):
    nombre_edificio= models.CharField(max_length=100)
    apartamento = models.CharField(max_length=80)
    habitaciones = models.CharField(max_length=60)
    propietario = models.CharField(max_length=60)
    banos = models.CharField(max_length=50)


def __str__(self):
    return 
    self.nombre_edificio+''+self.apartamento+''+self.habitaciones+''+self.propietario+''+self.banos

