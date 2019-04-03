from django.db import models
from django.utils import timezone
# Create your models here.


class Team_member(models.Model):
    name = models.CharField(max_length=200)
    consumption = models.CharField(max_length=500, default=[])
    consumed_products = models.CharField(max_length=500, default=[])

    def consume(self, consumed):
        #metodo para consumir producto, nombre producto y nro de veces
        products = []
        for tup in consumed:
            if int(tup[1]):
                continue
            if tup[1] > 0:
                products.append(tup[0])

        consumption = consumed
        consumed_products = products

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
