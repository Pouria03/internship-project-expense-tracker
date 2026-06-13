from django.contrib import admin
from django.urls import path, include
from apps.expenses.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('apps.accounts.urls')),
    path('categories/', include('apps.expenses.urls.category_urls')),
    path('expenses/', include('apps.expenses.urls.expense_urls')),
    path('stats/', include('apps.expenses.urls.stats_urls')),
    path('export/', include('apps.expenses.urls.excel_urls')),
    path('', home_view, name='home'),
]