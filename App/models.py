from django.db import models
from Auth.models import MyUser, Level


class Classroom(models.Model):

    slug = models.CharField(max_length=200)
    capacity = models.IntegerField()
    desc = models.TextField(null=True, blank=True)
    created_by = models.ForeignKey(
        MyUser, on_delete=models.SET_NULL, null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.slug

    def serialize(self):
        return {
            'id': self.id,
            'slug': self.slug,
            'desc': self.desc,
            'capacity': self.capacity,
        }


class Subject(models.Model):

    slug = models.CharField(max_length=200)
    code = models.CharField(max_length=200, null=True, blank=True)
    total_time = models.IntegerField()
    level = models.ForeignKey(Level, on_delete=models.SET_NULL, null=True)
    desc = models.TextField(null=True, blank=True)
    bgColor = models.CharField(max_length=20, null=True)
    created_by = models.ForeignKey(
        MyUser, on_delete=models.SET_NULL, null=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.slug

    def serialize(self):
        return {
            'id': self.id,
            'slug': self.slug,
            'desc': self.desc,
            'code': self.code,
            'total_time': self.total_time,
            'level': self.level.serialize()
        }


class Timetable(models.Model):

    teacher = models.ForeignKey(MyUser, on_delete=models.SET_NULL, null=True)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)
    classroom = models.ForeignKey(
        Classroom, on_delete=models.SET_NULL, null=True)

    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    start_time = models.TimeField(null=True)
    end_time = models.TimeField(null=True)

    updated_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"du {self.start_date} au {self.end_date}"

    def serialize(self):
        return {
            'id': self.id,
            'title': self.subject.slug,
            'start': f"{self.start_date}T{self.start_time}",
            'end': f"{self.end_date}T{self.start_time}",
            'teacher': self.teacher.serialize(),
            'subject': self.subject.serialize(),
            'classroom': self.classroom.serialize(),
            'className': "fc-event-danger",
        }
