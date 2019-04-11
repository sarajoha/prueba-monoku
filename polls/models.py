from django.db import models
from django.utils import timezone
# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    #agregar campo de cantidad total, que seria el inventario

    def __str__(self):
        return self.name


class Consumption(models.Model):
    quantity = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
#el consumo no puede ser mayor a lo que haya en el inventario
#cada vez que haya un consumo se debe restar del inventario

    def __str__(self):
        return '%s %s' % (self.product, self.quantity)


class Team_member(models.Model):
    name = models.CharField(max_length=200, unique=True)
    products = models.ManyToManyField(Product)
    consumptions = models.ManyToManyField(Consumption)

    def __str__(self):
        return self.name
