# Generated by Django 3.0.8 on 2020-11-03 11:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0004_auto_20201102_2201'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(blank=True, default='default.png', null=True, upload_to='Profile_images'),
        ),
    ]
