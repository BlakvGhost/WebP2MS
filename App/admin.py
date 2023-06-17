from django.contrib import admin
from . import models

admin.site.register(models.Classrooms)
admin.site.register(models.Levels)
admin.site.register(models.Timetables)
admin.site.register(models.Subjects)