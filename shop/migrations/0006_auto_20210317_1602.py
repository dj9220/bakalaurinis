# Generated by Django 3.1.7 on 2021-03-17 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_auto_20210317_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.CharField(default='data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAMAAAAJbSJIAAAAgVBMVEX///8AAADg4OCGhobl5eWysrL5+fnz8/NFRUX7+/v29vbPz8/y8vLa2tplZWXs7OysrKwwMDCkpKS/v78+Pj44ODgeHh51dXUXFxdYWFiTk5NSUlKamprU1NR6enqKioptbW0MDAwrKyvFxcUdHR1KSkq6urpnZ2cLCwtdXV1UVFTPDXCVAAAGtElEQVR4nO2d6XbiMAyFcUhpKGFfS0vZCjP0/R9w2Gag5dqWnYClOf5+xxxdYsvyEqlSiUQikUgkEolEIpFIJBIpTL3Wbs4azeSlFtqSO5A3ex/ZUv1l1Zr309A2lUi+3Y3ULdl8FtqycmgsgLozo578Dtvv6vUdqbZDm1iIxsCi78D0JbSZ3uSG/vmtr25DW+rJlqbvQEvia6yP6QKVmshzq+3MReCeTmiLHUknjgL3Die0zU', max_length=500),
        ),
    ]
