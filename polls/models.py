from django.db import models
from django.utils import timezone
# Create your models here.

class Team_member(models.Model):
    name = models.CharField(max_length=200)
    CONSUME = []
    PRODUCTOS = []
    consumo_total = models.CharField(max_length=200, default=CONSUME)
    consumo_productos = models.CharField(max_length=200, default=PRODUCTOS)

    def consumir(self, producto, cantidad):
        #metodo para consumir producto, nombre producto y nro de veces
        if int(cantidad):
            CONSUME.append((producto, cantidad))
        else:
            return "Valores no validos"

        if cantidad > 0:
            PRODUCTOS.append(producto)


class Producto(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
