
from django.urls import path

from . import views

urlpatterns = [
    path('expenses/', views.my_expenses, name='expenses'),
]