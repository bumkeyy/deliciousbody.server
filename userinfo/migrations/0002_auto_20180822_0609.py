# Generated by Django 2.1 on 2018-08-22 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='avatar',
            field=models.ImageField(default='/impyage.jpg', upload_to=''),
        ),
    ]