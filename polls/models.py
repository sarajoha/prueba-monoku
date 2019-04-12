from django.db import models
from django.utils import timezone
# Create your models here.


class Team_member(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    quantity = models.PositiveIntegerField(null=True)

    def __str__(self):
        return '%s %s' % (self.name, self.quantity)


class Consumption(models.Model):
    team_member = models.ForeignKey(Team_member, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.PositiveIntegerField()
#el consumo no puede ser mayor a lo que haya en el inventario
#cada vez que haya un consumo se debe restar del inventario

    def __str__(self):
        return '%s %s %s' % (self.team_member, self.product, self.quantity)
