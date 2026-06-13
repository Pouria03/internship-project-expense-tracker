from apps.expenses.repositories.expense_repository import ExpenseRepository


class ExpenseService:
    def __init__(self):
        self.repo = ExpenseRepository()

    def get_user_expenses(self, user):
        return self.repo.get_user_expenses(user)

    def get_expense(self, expense_id):
        return self.repo.get_by_id(expense_id)

    def create_expense(self, user, category, title, quantity, amount, description, evaluation):
        title = title.strip()
        if not title:
            raise ValueError('عنوان هزینه نمی‌تواند خالی باشد.')
        if quantity < 1:
            raise ValueError('مقدار باید حداقل ۱ باشد.')
        if amount < 0:
            raise ValueError('مبلغ نمی‌تواند منفی باشد.')
        if not category:
            raise ValueError('دسته‌بندی الزامی است.')

        return self.repo.create(
            user=user,
            category=category,
            title=title,
            quantity=quantity,
            amount=amount,
            description=description.strip(),
            evaluation=evaluation
        )

    def update_expense(self, expense, **kwargs):
        if 'title' in kwargs:
            kwargs['title'] = kwargs['title'].strip()
            if not kwargs['title']:
                raise ValueError('عنوان هزینه نمی‌تواند خالی باشد.')
        if 'quantity' in kwargs and kwargs['quantity'] < 1:
            raise ValueError('مقدار باید حداقل ۱ باشد.')
        if 'amount' in kwargs and kwargs['amount'] < 0:
            raise ValueError('مبلغ نمی‌تواند منفی باشد.')
        if 'description' in kwargs:
            kwargs['description'] = kwargs['description'].strip()

        return self.repo.update(expense, **kwargs)

    def delete_expense(self, expense):
        self.repo.delete(expense)