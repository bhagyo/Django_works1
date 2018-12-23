
from django.urls import path

from . import views

urlpatterns = [
    path('expenses/', views.my_expenses, name='expenses'),
    path('add-expenses/', views.add_expenses, name='add-expenses'),
    path('edit/<int:expense_id>/', views.edit_expenses, name='edit'),
    path('delete/<int:expense_id>/', views.delete_expense, name='delete'),
]
