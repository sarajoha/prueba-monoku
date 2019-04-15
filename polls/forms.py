from django import forms

from .models import Consumption, Product

class ConsumptionForm(forms.ModelForm):

    team_member = Consumption.objects.values('team_member__name')
    product = Consumption.objects.values('product__name')

    class Meta:
        model = Consumption

        fields = ('team_member', 'product', 'quantity')

    def clean_quantity(self):
        data = self.cleaned_data['quantity']
        data_prod = self.cleaned_data['product']
        prod = Product.objects.get(id=data_prod.id)

        if data <= 0:
            self.add_error('quantity' ,'La cantidad debe ser mayor a 0')

        elif data > prod.quantity:
            raise forms.ValidationError('La cantidad no puede ser mayor a lo que hay en el inventario')

        return data
