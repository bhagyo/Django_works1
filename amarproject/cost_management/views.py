from django.shortcuts import render, redirect
from .models import Expenses
from .forms import ExpenseForm
# Create your views here.


def my_expenses(request):
    expenses = Expenses.objects.all()
    return render(request, 'cost/expenses.html', {'expenses': expenses})


def add_expenses(request):
    print("in add expenses----------")
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        form.save()
        return redirect('expenses')
    else:
        form = ExpenseForm
    return render(request, 'cost/add_expenses.html', {'form': form})
