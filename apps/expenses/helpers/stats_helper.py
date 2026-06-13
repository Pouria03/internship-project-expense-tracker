from collections import defaultdict
from apps.expenses.helpers.jalali_helper import to_jalali


def get_category_summary(expenses):
    """جمع مبالغ به تفکیک دسته‌بندی"""
    summary = defaultdict(int)
    for expense in expenses:
        summary[expense.category.name] += expense.quantity * expense.amount
    return dict(summary)


def get_monthly_summary(expenses):
    """جمع مبالغ به تفکیک ماه"""
    summary = defaultdict(int)
    for expense in expenses:
        month_key = to_jalali(expense.created_at)[:7]  # e.g. 1405/03
        summary[month_key] += expense.quantity * expense.amount
    return dict(sorted(summary.items()))


def get_total_spent(expenses):
    """کل هزینه"""
    return sum(e.quantity * e.amount for e in expenses)


def get_evaluation_summary(expenses):
    """تعداد به تفکیک ارزیابی"""
    from collections import Counter
    labels = {'bad': 'بد', 'average': 'متوسط', 'good': 'خوب', 'excellent': 'عالی'}
    counter = Counter(e.evaluation for e in expenses)
    return {labels[k]: v for k, v in counter.items()}