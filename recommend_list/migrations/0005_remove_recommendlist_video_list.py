# Generated by Django 2.1 on 2018-10-09 08:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recommend_list', '0004_auto_20181009_0803'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recommendlist',
            name='video_list',
        ),
    ]
