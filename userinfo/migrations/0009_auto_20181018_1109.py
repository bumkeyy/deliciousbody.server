# Generated by Django 2.1 on 2018-10-18 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0008_auto_20181018_0431'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='name',
            field=models.CharField(default='name', max_length=30),
        ),
    ]
