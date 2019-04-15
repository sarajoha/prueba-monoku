from polls.models import Consumption, Team_member, Product

def run():

    table = [('Pringles', 0), ('Jumbo', 14), ('Tosh', 44), ('Cocosette', 23),
    ('Frunas', 46), ('Jet', 4), ('Gala Miti', 5), ('Chocorramos', 18),
    ('Club Social', 8), ('Gansito', 0), ('Bon bon bum', 29), ('Achiras', 0),
    ('Bridge', 8), ('Chips Ahoy', 0), ('Crispetas', 16), ('Saltin Noel', 7),
    ('Ritz', 0)]

    for tup in table:
        prod = Product.objects.get(name=tup[0])
        prod.quantity = tup[1]
        prod.save()
