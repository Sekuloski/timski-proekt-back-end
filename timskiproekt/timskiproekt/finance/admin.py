from django.contrib import admin
from .models import Purchase, ExpenseType, Addition
# Register your models here.

admin.site.register(Purchase)
admin.site.register(ExpenseType)
admin.site.register(Addition)
