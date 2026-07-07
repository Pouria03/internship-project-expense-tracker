from django.contrib import admin
from django.urls import path, include
from apps.expenses.views import home_view, about_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('apps.accounts.urls')),
    path('categories/', include('apps.expenses.urls.category_urls')),
    path('expenses/', include('apps.expenses.urls.expense_urls')),
    path('stats/', include('apps.expenses.urls.stats_urls')),
    path('export/', include('apps.expenses.urls.excel_urls')),
    path('about/', about_view, name='about'),
    path('', home_view, name='home'),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)