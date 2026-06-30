from apps.expenses.models import Expense


class ExpenseRepository:
    @staticmethod
    def get_user_expenses(user):
        return Expense.objects.filter(user=user).select_related('category').order_by('-created_at')

    @staticmethod
    def get_by_id(expense_id):
        return Expense.objects.filter(id=expense_id).first()

    @staticmethod
    def create(user, category, title, quantity, amount, description, evaluation, created_at=None):
        kwargs = dict(
            user=user,
            category=category,
            title=title,
            quantity=quantity,
            amount=amount,
            description=description,
            evaluation=evaluation,
        )
        if created_at is not None:
            kwargs['created_at'] = created_at
        return Expense.objects.create(**kwargs)

    @staticmethod
    def update(expense, **kwargs):
        for field, value in kwargs.items():
            setattr(expense, field, value)
        expense.save()
        return expense

    @staticmethod
    def delete(expense):
        expense.delete()