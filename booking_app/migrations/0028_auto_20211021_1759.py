# Generated by Django 2.2 on 2021-10-21 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0027_auto_20211021_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='viewer',
            field=models.CharField(default='', max_length=1000),
        ),
    ]