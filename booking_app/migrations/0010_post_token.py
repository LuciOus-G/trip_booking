# Generated by Django 2.2 on 2021-02-22 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0009_auto_20210221_2037'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Token',
            field=models.CharField(blank=True, default=None, editable=False, max_length=255, unique=True),
        ),
    ]