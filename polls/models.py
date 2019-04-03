from django.db import models
from django.utils import timezone
# Create your models here.
#poner todo en ingles!!

class Team_member(models.Model):
    name = models.CharField(max_length=200)
    consumo_total = models.CharField(max_length=500)
    consumo_productos = models.CharField(max_length=500)

    def consumir(self, consumo):
        #metodo para consumir producto, nombre producto y nro de veces
        productos = []
        for tup in consumo:
            if int(tup[1]):
                continue
            if tup[1] > 0:
                productos.append(tup[0])

        consumo_total = consumo
        consumo_productos = productos

    def __str__(self):
        return self.name


class Producto(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
