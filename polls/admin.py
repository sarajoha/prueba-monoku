from django.contrib import admin
from .models import Team_member, Product, Consumption
from django.db.models import Avg, Max, Min, Sum, Count


class ConsumptionAdmin(admin.ModelAdmin):
    # def get_queryset(self, request):
    #     qs = super().get_queryset(request)
    #     return qs.distinct()

    def aggregate_consumptions(self, request):

        qs = super(ConsumptionAdmin, self).get_queryset(request)

        return qs.filter(team_member=request.team_member).filter(product=request.product).aggregate(Sum('quantity'))


    list_display = ('team_member', 'product', 'aggregate_consumptions')

    list_filter = ('team_member',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity')


# Register your models here.
admin.site.register(Team_member)
admin.site.register(Product, ProductAdmin)
admin.site.register(Consumption, ConsumptionAdmin)
