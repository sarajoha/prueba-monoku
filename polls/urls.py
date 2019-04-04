from django.urls import path
from . import views

urlpatterns = [
    path('', views.answers, name='answers'),
]
