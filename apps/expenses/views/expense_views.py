from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from apps.expenses.services.expense_service import ExpenseService
from apps.expenses.services.category_service import CategoryService
from apps.expenses.models import Expense
from apps.expenses.helpers.jalali_helper import to_jalali

expense_service = ExpenseService()
category_service = CategoryService()


@login_required
def expense_list(request):
    expenses = expense_service.get_user_expenses(request.user)
    for expense in expenses:
        expense.jalali_date = to_jalali(expense.created_at)
    return render(request, 'expenses/list.html', {'expenses': expenses})


@login_required
def expense_create(request):
    categories = category_service.get_user_categories(request.user)
    if request.method == 'POST':
        try:
            category = category_service.get_category(request.POST.get('category'))
            if not category or category.user != request.user:
                raise ValueError('دسته‌بندی نامعتبر است.')

            expense_service.create_expense(
                user=request.user,
                category=category,
                title=request.POST.get('title', ''),
                quantity=int(request.POST.get('quantity', 1)),
                amount=int(request.POST.get('amount', 0)),
                description=request.POST.get('description', ''),
                evaluation=request.POST.get('evaluation', 'average')
            )
            messages.success(request, 'هزینه با موفقیت ثبت شد.', extra_tags='success')
            return redirect('expenses:expense_list')
        except ValueError as e:
            messages.error(request, str(e), extra_tags='danger')

    return render(request, 'expenses/create.html', {
        'categories': categories,
        'evaluation_choices': Expense.Evaluation.choices
    })


@login_required
def expense_update(request, pk):
    expense = get_object_or_404(Expense, id=pk, user=request.user)
    categories = category_service.get_user_categories(request.user)

    if request.method == 'POST':
        try:
            category = category_service.get_category(request.POST.get('category'))
            if not category or category.user != request.user:
                raise ValueError('دسته‌بندی نامعتبر است.')

            expense_service.update_expense(
                expense=expense,
                category=category,
                title=request.POST.get('title', ''),
                quantity=int(request.POST.get('quantity', 1)),
                amount=int(request.POST.get('amount', 0)),
                description=request.POST.get('description', ''),
                evaluation=request.POST.get('evaluation', 'average')
            )
            messages.success(request, 'هزینه با موفقیت ویرایش شد.', extra_tags='success')
            return redirect('expenses:expense_list')
        except ValueError as e:
            messages.error(request, str(e), extra_tags='danger')

    return render(request, 'expenses/update.html', {
        'expense': expense,
        'categories': categories,
        'evaluation_choices': Expense.Evaluation.choices
    })


@login_required
def expense_delete(request, pk):
    expense = get_object_or_404(Expense, id=pk, user=request.user)
    if request.method == 'POST':
        expense_service.delete_expense(expense)
        messages.success(request, 'هزینه با موفقیت حذف شد.', extra_tags='success')
    return redirect('expenses:expense_list')