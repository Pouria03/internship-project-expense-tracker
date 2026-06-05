from django.urls import path
from apps.expenses.views.category_views import category_list, category_create, category_update, category_delete

app_name = 'categories'

urlpatterns = [
    path('', category_list, name='category_list'),
    path('create/', category_create, name='category_create'),
    path('update/<int:pk>/', category_update, name='category_update'),
    path('delete/<int:pk>/', category_delete, name='category_delete'),
]