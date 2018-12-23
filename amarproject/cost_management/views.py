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


def edit_expenses(request, expense_id):
    expense = Expenses.objects.get(id=expense_id)
    if request.method == 'POST':
        form = ExpenseForm(request.POST, instance=expense)
        form.save()
        return redirect('expenses')
    else:
        form = ExpenseForm(instance=expense)
    return render(request, 'cost/edit_expenses.html', {'form': form})


def delete_expense(request, expense_id):
    expense = Expenses.objects.get(id=expense_id)
    expense.delete()
    return redirect('expenses')


"""
def edit_expenses(request, expense_id):

    instance = Expenses.objects.get(id=expense_id)
    form = ExpenseForm(request.POST, instance=instance)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('expenses')
    return request(request, 'cost/edit_expenses.html', {'form': form})
"""
