from django.shortcuts import render

# Create your views here.
def answers(request):
    return render(request, 'polls/answers.html', {})
