from django.urls import path
from apps.expenses.views.stats_views import stats

app_name = 'stats'

urlpatterns = [
    path('', stats, name='stats'),
]