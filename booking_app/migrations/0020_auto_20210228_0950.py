# Generated by Django 2.2 on 2021-02-28 02:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0019_auto_20210228_0904'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='photo2',
        ),
        migrations.RemoveField(
            model_name='post',
            name='photo3',
        ),
    ]
