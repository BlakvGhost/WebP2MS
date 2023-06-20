from django.contrib import admin
from .models import MyUser, Level

# Register your models here.

admin.site.register(MyUser)
admin.site.register(Level)