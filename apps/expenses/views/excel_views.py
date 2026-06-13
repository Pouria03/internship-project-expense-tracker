from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from apps.expenses.services.expense_service import ExpenseService
from apps.expenses.helpers.excel_helper import export_expenses_to_excel
from apps.expenses.helpers.jalali_helper import to_jalali
from jdatetime import datetime as jdatetime

expense_service = ExpenseService()


@login_required
def export_excel(request):
    expenses = expense_service.get_user_expenses(request.user)
    excel_file = export_expenses_to_excel(expenses)

    today = to_jalali(jdatetime.now())

    response = HttpResponse(
        excel_file.getvalue(),
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = f'attachment; filename="expenses_{today}.xlsx"'
    return response