# Generated by Django 2.2 on 2020-10-22 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0003_booking_name_trip'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='price',
            field=models.CharField(default=None, max_length=20),
        ),
    ]
