# Generated by Django 2.1 on 2018-09-02 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='thumbnail_url',
        ),
        migrations.AddField(
            model_name='video',
            name='video_file',
            field=models.FileField(default=1, upload_to='video/%Y/%m/%d'),
            preserve_default=False,
        ),
    ]