from django.shortcuts import render
from .models import Expenses
# Create your views here.


def my_expenses(request):
    expenses = Expenses.objects.all()
    return render(request, 'expenses.html', {'expenses': expenses})
