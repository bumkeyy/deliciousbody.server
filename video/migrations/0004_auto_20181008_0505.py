# Generated by Django 2.1 on 2018-10-08 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_auto_20181007_1829'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='part1',
        ),
        migrations.RemoveField(
            model_name='video',
            name='part2',
        ),
        migrations.RemoveField(
            model_name='video',
            name='part3',
        ),
        migrations.RemoveField(
            model_name='video',
            name='part4',
        ),
        migrations.RemoveField(
            model_name='video',
            name='part5',
        ),
        migrations.RemoveField(
            model_name='video',
            name='part6',
        ),
        migrations.RemoveField(
            model_name='video',
            name='part7',
        ),
        migrations.RemoveField(
            model_name='video',
            name='part8',
        ),
        migrations.AddField(
            model_name='video',
            name='main_part',
            field=models.IntegerField(default=0, verbose_name='주 운동부위'),
        ),
        migrations.AddField(
            model_name='video',
            name='sub_part',
            field=models.IntegerField(default=0, verbose_name='부 운동부위'),
        ),
    ]
