import json
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apps.expenses.services.expense_service import ExpenseService
from apps.expenses.helpers.stats_helper import get_category_summary, get_monthly_summary, get_total_spent, get_evaluation_summary
from apps.expenses.helpers.jalali_helper import to_jalali

expense_service = ExpenseService()


@login_required
def stats(request):
    expenses = expense_service.get_user_expenses(request.user)

    total_spent = get_total_spent(expenses)
    category_summary = get_category_summary(expenses)
    monthly_summary = get_monthly_summary(expenses)
    evaluation_summary = get_evaluation_summary(expenses)

    for expense in expenses:
        expense.jalali_date = to_jalali(expense.created_at)

    context = {
        'expenses': expenses[:10],
        'total_spent': total_spent,
        'total_count': len(expenses),
        'chart_data': json.dumps({
            'category_labels': list(category_summary.keys()),
            'category_data': [int(v) for v in category_summary.values()],
            'monthly_labels': list(monthly_summary.keys()),
            'monthly_data': [int(v) for v in monthly_summary.values()],
            'evaluation_labels': list(evaluation_summary.keys()),
            'evaluation_data': [int(v) for v in evaluation_summary.values()],
        }, ensure_ascii=False),
    }
    return render(request, 'expenses/stats.html', context)