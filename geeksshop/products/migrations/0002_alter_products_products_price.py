# Generated by Django 3.2.7 on 2021-09-28 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='products_price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]