# Generated by Django 2.1 on 2018-10-07 16:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_name', models.CharField(max_length=50)),
                ('video_id', models.IntegerField(default=0)),
                ('level', models.IntegerField(default=2, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)])),
                ('part1', models.BooleanField(default=True)),
                ('part2', models.BooleanField(default=False)),
                ('part3', models.BooleanField(default=False)),
                ('part4', models.BooleanField(default=False)),
                ('part5', models.BooleanField(default=False)),
                ('part6', models.BooleanField(default=False)),
                ('part7', models.BooleanField(default=False)),
                ('part8', models.BooleanField(default=False)),
                ('time', models.IntegerField()),
                ('description', models.TextField(max_length=300)),
                ('video_url', models.TextField(validators=[django.core.validators.URLValidator()])),
                ('video_file', models.TextField(validators=[django.core.validators.URLValidator()])),
                ('video_thumbnail', models.TextField(validators=[django.core.validators.URLValidator()])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
