# Generated by Django 2.1 on 2018-10-08 06:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0004_auto_20181008_0505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_url',
            field=models.TextField(blank=True, null=True, validators=[django.core.validators.URLValidator()]),
        ),
    ]
