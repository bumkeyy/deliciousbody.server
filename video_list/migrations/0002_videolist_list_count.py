# Generated by Django 2.1 on 2018-10-09 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videolist',
            name='list_count',
            field=models.IntegerField(default=0),
        ),
    ]
