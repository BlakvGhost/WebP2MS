# Generated by Django 4.2.2 on 2023-06-18 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0010_level_myuser_phone_num_myuser_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='total_students',
            field=models.IntegerField(default=200),
        ),
    ]
