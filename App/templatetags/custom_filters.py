from django import template
from django.db.models import Sum
from App.models import Timetable
from django.db import models
from datetime import timedelta


register = template.Library()

@register.filter
def calculate_total_hours(subject_id):
    total_hours = Timetable.objects.filter(subject_id=subject_id).aggregate(
        total=Sum(models.F('end_time') - models.F('start_time')))['total']
    return total_hours if total_hours is not None else 0

@register.filter
def calculate_total_percentage(subject):
    #total_hours = (calculate_total_hours(subject.id) * 100) / timedelta(hours=subject.total_time)
    return subject.total_time

