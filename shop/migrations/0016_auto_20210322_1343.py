# Generated by Django 3.1.7 on 2021-03-22 13:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0015_auto_20210322_1346'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='subCategory',
        ),
        migrations.AddField(
            model_name='category',
            name='subcategories',
            field=models.ManyToManyField(blank=True, related_name='_category_subcategories_+', to='shop.Category'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.supplier'),
        ),
        migrations.DeleteModel(
            name='SubCategories',
        ),
    ]
