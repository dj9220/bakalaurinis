# Generated by Django 3.0.8 on 2021-05-04 11:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0042_auto_20210503_1420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
    ]
