from django import forms

from .models import Consumption

class ConsumptionForm(forms.ModelForm):

    team_member = Consumption.objects.values('team_member__name')
    product = Consumption.objects.values('product__name')

    class Meta:
        model = Consumption

        fields = ('team_member', 'product', 'quantity')
