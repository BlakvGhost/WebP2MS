from django.db import models
from Auth.models import MyUser, Level
from django.contrib.humanize.templatetags import humanize


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
    bgColor = models.CharField(max_length=255, null=True, blank=True)
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
            'title': f"{self.subject.slug} de {self.subject.level.slug}",
            'start': f"{self.start_date}T{self.start_time}",
            'end': f"{self.end_date}T{self.end_time}",
            'start_time': self.start_time,
            'end_time': self.end_time,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'teacher': self.teacher.serialize(),
            'subject': self.subject.serialize(),
            'classroom': self.classroom.serialize(),
            'color': f"{self.subject.bgColor}",
        }


class Notification(models.Model):
    user = models.ForeignKey(
        MyUser, on_delete=models.CASCADE, related_name='notifications')
    message = models.CharField(max_length=255)
    is_opened = models.BooleanField(default=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.message

    def serialize(self):
        return {
            'id': self.id,
            'user': self.user.serialize(),
            'message': self.message,
            'created_at': humanize.naturaltime(self.created_at),
        }

class Chat(models.Model):
    timetable = models.ForeignKey(
        Timetable, on_delete=models.CASCADE, related_name='chats')
    user = models.ForeignKey(
        MyUser, on_delete=models.CASCADE, related_name='chats')
    message = models.CharField(max_length=255)
    is_opened = models.BooleanField(default=False, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.message

    def serialize(self):
        return {
            'id': self.id,
            'shedule': self.timetable.serialize(),
            'from': self.user.serialize(),
            'message': self.message,
            'is_opened': self.is_opened,
            'created_at': humanize.naturaltime(self.created_at),
        }
