from django import template
from django.db.models import Sum
from App.models import Timetables
from django.db import models


register = template.Library()

@register.filter
def calculate_total_hours(subject_id):
    total_hours = Timetables.objects.filter(subject_id=subject_id).aggregate(
        total=Sum(models.F('end_time') - models.F('start_time')))['total']
    return total_hours if total_hours is not None else 0

