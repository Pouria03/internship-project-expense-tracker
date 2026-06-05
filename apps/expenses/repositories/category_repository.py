from apps.expenses.models import Category


class CategoryRepository:
    @staticmethod
    def get_user_categories(user):
        return Category.objects.filter(user=user).order_by('name')

    @staticmethod
    def get_by_id(category_id):
        return Category.objects.filter(id=category_id).first()

    @staticmethod
    def create(user, name):
        return Category.objects.create(user=user, name=name)

    @staticmethod
    def update(category, name):
        category.name = name
        category.save()
        return category

    @staticmethod
    def delete(category):
        category.delete()