# Generated by Django 3.0.8 on 2020-11-03 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registers', '0005_auto_20201103_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_img',
            field=models.ImageField(blank=True, default='image/default.png', null=True, upload_to='Profile_images'),
        ),
    ]
