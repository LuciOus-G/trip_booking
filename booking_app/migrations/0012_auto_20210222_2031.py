# Generated by Django 2.2 on 2021-02-22 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0011_auto_20210222_2030'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Trip', 'verbose_name_plural': 'Trip'},
        ),
    ]