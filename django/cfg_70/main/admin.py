from django.contrib import admin
from main.models import Employee, UserProfile

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Employee)