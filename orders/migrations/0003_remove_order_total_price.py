# Generated by Django 3.0.8 on 2020-12-20 04:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_total_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='total_price',
        ),
    ]
