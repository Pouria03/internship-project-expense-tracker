from django.urls import path
from apps.expenses.views.expense_views import expense_list, expense_create, expense_update, expense_delete

app_name = 'expenses'

urlpatterns = [
    path('', expense_list, name='expense_list'),
    path('create/', expense_create, name='expense_create'),
    path('update/<int:pk>/', expense_update, name='expense_update'),
    path('delete/<int:pk>/', expense_delete, name='expense_delete'),
]