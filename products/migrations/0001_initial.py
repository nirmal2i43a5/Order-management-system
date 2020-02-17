# Generated by Django 3.0.2 on 2020-02-17 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('price', models.CharField(max_length=50, null=True)),
                ('category', models.CharField(choices=[('indoor service', 'indoor service'), ('outdoor service', 'outdoor service')], max_length=200, null=True)),
                ('description', models.CharField(max_length=50, null=True)),
                ('created_at', models.DateField(auto_now=True, null=True)),
            ],
        ),
    ]
