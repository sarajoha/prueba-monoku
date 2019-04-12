from polls.models import Consumption, Team_member, Product

def run():

    table = {'Luis L': {'Achiras': 4, 'Bridge': 4, 'Club Social': 8, 'Cocosette': 4, 'Gala Miti': 12, 'Jet': 8, 'Pringles': 4, 'Tosh': 8},
    'Nata': {},
    'Leonel': {'Bon bon bum': 4, 'Club Social': 4, 'Cocosette': 4, 'Jet': 4, 'Pringles': 8},
    'Yeison': {'Bon bon bum': 8, 'Chocorramos': 4, 'Frunas': 16, 'Gala Miti': 16, 'Gansito': 8, 'Jet': 4, 'Jumbo': 4, 'Pringles': 16, 'Tosh': 16},
    'Jose': {'Club Social': 8, 'Cocosette': 8, 'Tosh': 4},
    'Brian': {'Club Social': 4, 'Chocorramos': 4, 'Frunas': 20, 'Gansito': 8, 'Jet': 8, 'Jumbo': 8, 'Tosh': 4},
    'Andres C': {'Chocorramos': 32, 'Frunas': 12, 'Gala Miti': 16, 'Gansito': 8, 'Jet': 8},
    'Andres A': {'Bridge': 8, 'Chocorramos': 4, 'Cocosette': 16, 'Frunas': 4, 'Jet': 8, 'Jumbo': 8, 'Tosh': 8},
    'Luis V': {'Club Social': 4, 'Cocosette': 8},
    'Julian': {'Achiras': 4, 'Bridge': 4, 'Chips Ahoy': 4, 'Cocosette': 4, 'Crispetas': 4, 'Jet': 4, 'Jumbo': 4, 'Pringles': 4, 'Ritz': 4, 'Tosh': 16},
    'Juan': {'Bon bon bum': 4, 'Cocosette': 4, 'Jumbo': 24},
    'Estefany': {'Chips Ahoy': 8, 'Cocosette': 16, 'Crispetas': 4, 'Gala Miti': 4, 'Jet': 4, 'Jumbo': 12, 'Pringles': 16},
    'Alejandra': {'Achiras': 8, 'Bon bon bum': 4, 'Club Social': 4, 'Frunas': 8, 'Gala Miti': 4, 'Jet': 8, 'Jumbo': 8, 'Pringles': 8, 'Saltin Noel': 8, 'Tosh': 12},
    'Elizabeth': {'Crispetas': 4, 'Pringles': 16}}

    for key, value in table.items():
        member = Team_member.objects.get(name=key)
        for item, inner_value in value.items():
            prod = Product.objects.get(name=item)
            Consumption.objects.create(team_member=member, product=prod, quantity=inner_value)
