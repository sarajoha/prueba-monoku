from django.shortcuts import render
from .models import Product, Consumption, Team_member
from django.db.models import Avg, Max, Min, Sum, Count

# Create your views here.
def answers(request):
    names = Team_member.objects.all() #for name in names do
    ate_the_most = Team_member.objects.annotate(sum=Sum('consumptions__quantity')).order_by('-sum').first()
    most_cons = Team_member.objects.values('consumptions__product__name').annotate(sum=Sum('consumptions__quantity')).order_by('-sum').first()
    most_consumed = most_cons['consumptions__product__name']

    return render(request, 'polls/answers.html', {'names': names, #'products': products,
                                                'ate_the_most': ate_the_most,
                                                'most_consumed': most_consumed})

def eat(request):
    names = Team_member.objects.all()
    products = Product.objects.all()
    return render(request, 'polls/eat.html', {'names': names, 'products': products})
