# Generated by Django 2.1.7 on 2019-05-20 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0005_auto_20190520_1750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='items',
            name='retailer',
        ),
    ]
