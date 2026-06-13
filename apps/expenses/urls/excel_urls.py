from django.urls import path
from apps.expenses.views.excel_views import export_excel

app_name = 'excel'

urlpatterns = [
    path('', export_excel, name='export'),
]   