# Generated by Django 4.1.3 on 2022-11-10 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='discount',
        ),
        migrations.AlterField(
            model_name='product',
            name='quantity',
            field=models.CharField(max_length=20),
        ),
    ]
