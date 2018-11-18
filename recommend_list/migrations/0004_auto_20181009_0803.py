# Generated by Django 2.1 on 2018-10-09 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('video_list', '0002_videolist_list_count'),
        ('recommend_list', '0003_auto_20181008_0607'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendlist',
            name='videolist',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='videolist', to='video_list.VideoList'),
        ),
        migrations.AlterField(
            model_name='recommendlist',
            name='video_list',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='video_list', to='video.Video'),
        ),
    ]