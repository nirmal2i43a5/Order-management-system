# Generated by Django 3.0.8 on 2020-12-15 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0003_auto_20200711_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='date_created',
            field=models.DateField(),
        ),
    ]