from django.contrib import admin
from .models import Team_member, Product, Consumption


class ConsumptionAdmin(admin.ModelAdmin):
    list_display = ('team_member', 'product', 'quantity')
    list_filter = ('team_member',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity')


# Register your models here.
admin.site.register(Team_member)
admin.site.register(Product, ProductAdmin)
admin.site.register(Consumption, ConsumptionAdmin)
