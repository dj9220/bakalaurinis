# Generated by Django 3.1.7 on 2021-03-26 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0023_remove_product_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productdescription',
            name='weight',
        ),
        migrations.AddField(
            model_name='product',
            name='quantity',
            field=models.FloatField(default=0),
        ),
    ]
