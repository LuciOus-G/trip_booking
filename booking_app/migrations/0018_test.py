# Generated by Django 2.2 on 2021-02-27 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0017_auto_20210227_1938'),
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=100)),
            ],
        ),
    ]
