from django.conf import settings
from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator


class Category(models.Model):
    """
    Expense categories created by each user.
    Examples: groceries, rent, bills, entertainment.
    """
    name = models.CharField(max_length=100)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='categories'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'categories'
        verbose_name_plural = 'Categories'
        unique_together = ['name', 'user']  # Each user can't have duplicate category names
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.user.username})"


class Expense(models.Model):
    """
    Daily expense record for a user.
    """
    class Evaluation(models.TextChoices):
        BAD = 'bad', 'بد'
        AVERAGE = 'average', 'متوسط'
        GOOD = 'good', 'خوب'
        EXCELLENT = 'excellent', 'عالی'

    title = models.CharField(max_length=200, verbose_name='عنوان ریز هزینه')
    quantity = models.PositiveIntegerField(
        default=1,
        validators=[MinValueValidator(1)],
        verbose_name='مقدار/تعداد'
    )
    amount = models.DecimalField(
        max_digits=12,
        decimal_places=0,
        validators=[MinValueValidator(0)],
        verbose_name='مبلغ هزینه'
    )
    description = models.TextField(blank=True, verbose_name='توضیحات')
    evaluation = models.CharField(
        max_length=10,
        choices=Evaluation.choices,
        default=Evaluation.AVERAGE,
        verbose_name='نمره ارزیابی'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,  # Don't delete expense if category is deleted
        related_name='expenses',
        verbose_name='دسته‌بندی'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='expenses',
        verbose_name='کاربر'
    )
    created_at = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ثبت')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='تاریخ ویرایش')

    class Meta:
        db_table = 'expenses'
        verbose_name = 'Expense'
        verbose_name_plural = 'Expenses'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['user', '-created_at']),
            models.Index(fields=['user', 'category']),
        ]

    def __str__(self):
        return f"{self.title} - {self.amount} تومان"

    @property
    def total(self):
        """Calculate total cost for this expense record."""
        return self.quantity * self.amount
    
