# Generated by Django 2.2 on 2021-02-21 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0008_auto_20210221_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='day',
            field=models.CharField(default=None, max_length=15),
        ),
    ]