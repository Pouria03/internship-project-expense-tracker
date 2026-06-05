from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from apps.expenses.services.category_service import CategoryService
from apps.expenses.models import Category

service = CategoryService()


@login_required
def category_list(request):
    categories = service.get_user_categories(request.user)
    return render(request, 'categories/list.html', {'categories': categories})


@login_required
def category_create(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        try:
            service.create_category(user=request.user, name=name)
            messages.success(request, 'دسته‌بندی با موفقیت ایجاد شد.', extra_tags='success')
            return redirect('categories:category_list')
        except ValueError as e:
            messages.error(request, str(e), extra_tags='danger')
    return render(request, 'categories/create.html')


@login_required
def category_update(request, pk):
    category = get_object_or_404(Category, id=pk, user=request.user)
    if request.method == 'POST':
        name = request.POST.get('name', '')
        try:
            service.update_category(category, name)
            messages.success(request, 'دسته‌بندی با موفقیت ویرایش شد.', extra_tags='success')
            return redirect('categories:category_list')
        except ValueError as e:
            messages.error(request, str(e), extra_tags='danger')
    return render(request, 'categories/update.html', {'category': category})


@login_required
def category_delete(request, pk):
    category = get_object_or_404(Category, id=pk, user=request.user)
    if request.method == 'POST':
        try:
            service.delete_category(category)
            messages.success(request, 'دسته‌بندی با موفقیت حذف شد.', extra_tags='success')
        except ValueError as e:
            messages.error(request, str(e), extra_tags='danger')
    return redirect('categories:category_list')



# note, because we have set unique_together(category, user),
# in the model design of category, by using something like:
# 'category = get_object_or_404(Category, id=pk, user=request.user)',
# we are checking the requested object to be owned by the right user.