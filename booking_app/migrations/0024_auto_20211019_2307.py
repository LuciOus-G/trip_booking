# Generated by Django 2.2 on 2021-10-19 16:07

from django.db import migrations, models
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('booking_app', '0023_auto_20211019_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carousel',
            name='image',
            field=models.ImageField(default=None, upload_to='media_thumbnail'),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo1',
            field=django_resized.forms.ResizedImageField(crop=None, default=None, force_format='JPEG', keep_meta=True, quality=75, size=[1980, 1080], upload_to='media_thumbnail'),
        ),
    ]