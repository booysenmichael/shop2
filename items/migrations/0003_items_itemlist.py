# Generated by Django 2.1.7 on 2019-05-25 04:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_shoplist_shoplistdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='items',
            name='itemList',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='items.shopListDetails'),
        ),
    ]