# Generated by Django 2.1 on 2018-11-27 15:35

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0002_auto_20181127_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='activity_level',
            field=models.IntegerField(choices=[(1, '저'), (2, '중'), (3, '고')], default=2, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)], verbose_name='활동 수준'),
        ),
    ]
