from django.contrib import admin
from django.urls import path, include
from apps.expenses.views import home_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('apps.accounts.urls')),
    path('', home_view, name='home'),
]