from polls.models import Product

#create products in db
def run():
    PRODUCTS = ['Achiras', 'Bon bon bum', 'Bridge', 'Chips Ahoy', 'Club Social',
                'Chocorramos', 'Crispetas', 'Frunas', 'Gala Miti', 'Gansito', 'Jet',
                'Jumbo', 'Pringles', 'Ritz', 'Saltin Noel', 'Tosh']
    for item in PRODUCTS:
        Product.objects.create(name=item)
