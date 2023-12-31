# Generated by Django 4.2.2 on 2023-06-15 21:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Auth', '0004_myuser_first_name_myuser_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='myuser',
            name='reset_token',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='reset_token_expiration',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
