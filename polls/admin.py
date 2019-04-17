from django.contrib import admin
from .models import Team_member, Product, Consumption
from django.db.models import Avg, Max, Min, Sum, Count


class ConsumptionAdmin(admin.ModelAdmin):

    def aggre_cons(self, obj):
        return obj.aggre_cons

    def aggregate_consumptions(self, request):
        qs = super(ConsumptionAdmin, self).get_queryset(request)
        return qs.Consumption.objects.values('product__name').annotate(aggre_cons=Sum('quantity'))

    list_display = ('team_member', 'product', 'quantity')
    list_filter = ('team_member',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity')


# Register your models here.
admin.site.register(Team_member)
admin.site.register(Product, ProductAdmin)
admin.site.register(Consumption, ConsumptionAdmin)
