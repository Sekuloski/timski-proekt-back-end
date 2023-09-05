import datetime

from django.db import models
from django.utils import timezone

from customers.models import CustomUser

# Create your models here.

ADDITION_TYPES = [
    (0, 'Salary'),
    (1, 'ATM'),
    (2, 'Sale')
]


class ExpenseType(models.Model):
    name: str = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Purchase(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    amount: int = models.IntegerField()
    description: str = models.CharField(max_length=255)
    date: datetime.datetime = models.DateTimeField(default=timezone.now)
    expense_type: ExpenseType = models.ForeignKey(ExpenseType, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.description


class Addition(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True, blank=True)
    amount: int = models.IntegerField()
    description: str = models.CharField(max_length=255)
    date: datetime.datetime = models.DateTimeField(default=timezone.now)
    addition_type: int = models.IntegerField(
        choices=ADDITION_TYPES,
        default=0,
        null=False
    )

    def __str__(self):
        return self.description
