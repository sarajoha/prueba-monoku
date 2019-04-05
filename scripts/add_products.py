from polls.models import Product, Team_member

def run():

    table = {'Luis L': ['Achiras', 'Bridge', 'Club Social', 'Cocosette', 'Gala Miti',
    'Jet', 'Pringles', 'Tosh'],
    'Nata': [],
    'Leonel': ['Bon bon bum', 'Club Social', 'Cocosette', 'Jet', 'Pringles'],
    'Yeison': ['Bon bon bum', 'Chocorramos', 'Frunas', 'Gala Miti', 'Gansito', 'Jet', 'Jumbo', 'Pringles', 'Tosh'],
    'Jose': ['Club Social', 'Cocosette', 'Tosh'],
    'Brian': ['Club Social', 'Chocorramos', 'Frunas', 'Gansito', 'Jet', 'Jumbo', 'Tosh'],
    'Andres C': ['Chocorramos', 'Frunas', 'Gala Miti', 'Gansito', 'Jet'],
    'Andres A': ['Bridge', 'Chocorramos', 'Cocosette', 'Frunas', 'Jet', 'Jumbo', 'Tosh'],
    'Luis V': ['Club Social', 'Cocosette'],
    'Julian': ['Achiras', 'Bridge', 'Chips Ahoy', 'Cocosette', 'Crispetas', 'Jet', 'Jumbo', 'Pringles', 'Ritz', 'Tosh'],
    'Juan': ['Bon bon bum', 'Cocosette', 'Jumbo'],
    'Estefany': ['Chips Ahoy', 'Cocosette', 'Crispetas', 'Gala Miti', 'Jet', 'Jumbo', 'Pringles'],
    'Alejandra': ['Achiras', 'Bon bon bum', 'Club Social', 'Frunas', 'Gala Miti', 'Jet', 'Jumbo', 'Pringles', 'Saltin Noel', 'Tosh'],
    'Elizabeth': ['Crispetas', 'Pringles']}

    for key, value in table.items():
        member = Team_member.objects.get(name=key)
        for item in value:
            prod = Product.objects.get(name=item)
            member.products.add(prod)
