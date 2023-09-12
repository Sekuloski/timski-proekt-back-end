from django.contrib import admin

# Register your models here.
from customers.models import CustomUser

# Register your models here.
admin.site.register(CustomUser)
