from django import forms

from .models import Consumption, Product

class ConsumptionForm(forms.ModelForm):

    #product = Product.objects.filter(quantity__gt=0)
    product = forms.ModelChoiceField(queryset=Product.objects.filter(quantity__gt=0), label='Producto')

    class Meta:
        model = Consumption

        fields = ('team_member', 'product', 'quantity')
        labels = {'team_member': 'Miembro', 'quantity': 'Cantidad'}
        

    def clean_quantity(self):
        #fix this to
        data = self.cleaned_data['quantity']
        data_prod = self.cleaned_data['product']
        prod = Product.objects.get(id=data_prod.id)

        if data <= 0:
            self.add_error('quantity' ,'La cantidad debe ser mayor a 0')

        elif data > prod.quantity:
            raise forms.ValidationError('La cantidad no puede ser mayor a lo que hay en el inventario')

        return data
