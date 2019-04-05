from polls.models import Team_member

#create products in db
def run():
    MEMBERS = ['Luis L', 'Nata', 'Leonel', 'Yeison', 'Brian', 'Andres C', 'Andres A',
                'Luis V', 'Julian', 'Juan', 'Estefany', 'Alejandra', 'Elizabeth', 'Jose']

    for member in MEMBERS:
        Team_member.objects.create(name=member)
