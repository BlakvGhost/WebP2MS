# Generated by Django 4.2.2 on 2023-06-19 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_classroom_subject_timetable_remove_levels_created_by_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subject',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]
