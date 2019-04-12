from django.shortcuts import render, redirect
from .models import Product, Consumption, Team_member
from django.db.models import Avg, Max, Min, Sum, Count
from .forms import ConsumptionForm

# Create your views here.
def answers(request, name=None):
    names = Team_member.objects.all() #for name in names do
    consumption = Consumption.objects.values('product__name')
    #Consumption.objects.values('product__name').filter(team_member__name='Nata').distinct()
    #Consumption.objects.values('product__name').filter(team_member=name).distinct()

    ate_most = Consumption.objects.values('team_member__name').annotate(sum=Sum('quantity')).order_by('-sum').first()
    ate_the_most = ate_most['team_member__name']

    most_cons = Consumption.objects.values('product__name').annotate(sum=Sum('quantity')).order_by('-sum').first()
    most_consumed = most_cons['product__name']

    return render(request, 'polls/answers.html', {'names': names, 'consumption': consumption,
                                                'name': name,
                                                'ate_the_most': ate_the_most,
                                                'most_consumed': most_consumed,
                                                })

def eat(request):

    if request.method == "POST":
        form = ConsumptionForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('answers')
    else:
        form = ConsumptionForm()
    return render(request, 'polls/eat.html', {'form': form,})
