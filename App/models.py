from django.db import models

from Auth.models import MyUser, Level


class Classroom(models.Model):
    
    slug = models.CharField(max_length=200)
    capacity = models.IntegerField()
    created_by = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.slug
    

class Subject(models.Model):
    
    slug = models.CharField(max_length=200)
    code = models.CharField(max_length=200, null=True, blank=True)
    total_time = models.IntegerField()
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True)
    created_by = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.slug
    
class Timetable(models.Model):
    
    teach_by = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    classroom = models.ForeignKey(Classroom, on_delete=models.SET_NULL, null=True)
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True)
    week = models.IntegerField()
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return f"semaine {self.week}"