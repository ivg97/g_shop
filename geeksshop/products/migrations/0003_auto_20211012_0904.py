# Generated by Django 3.2.7 on 2021-10-12 09:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_products_products_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoryproducts',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='products',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
