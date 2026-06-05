from apps.expenses.repositories.category_repository import CategoryRepository
from django.db import IntegrityError


class CategoryService:
    def __init__(self):
        self.repo = CategoryRepository()

    def get_user_categories(self, user):
        return self.repo.get_user_categories(user)

    def get_category(self, category_id):
        return self.repo.get_by_id(category_id)

    def create_category(self, user, name):
        name = name.strip()
        if not name:
            raise ValueError('نام دسته‌بندی نمی‌تواند خالی باشد.')
        try:
            return self.repo.create(user=user, name=name)
        except IntegrityError:
            raise ValueError('این دسته‌بندی قبلاً ثبت شده است.')

    def update_category(self, category, name):
        name = name.strip()
        if not name:
            raise ValueError('نام دسته‌بندی نمی‌تواند خالی باشد.')
        try:
            return self.repo.update(category, name)
        except IntegrityError:
            raise ValueError('این دسته‌بندی قبلاً ثبت شده است.')

    def delete_category(self, category):
        if category.expenses.exists():
            raise ValueError('دسته‌بندی دارای هزینه است و نمی‌توان آن را حذف کرد.')
        self.repo.delete(category)