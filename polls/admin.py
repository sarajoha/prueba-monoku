from django.contrib import admin
from .models import Team_member, Product, Consumption


# Register your models here.
admin.site.register(Team_member)
admin.site.register(Product)
admin.site.register(Consumption)
