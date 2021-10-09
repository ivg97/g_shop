# Generated by Django 3.2.7 on 2021-09-26 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50, unique=True)),
                ('category_description', models.TextField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('products_name', models.CharField(max_length=50)),
                ('products_descriptions', models.TextField(blank=True, max_length=200)),
                ('products_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('image', models.ImageField(blank=True, upload_to='products_image')),
                ('quantity', models.PositiveIntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.categoryproducts')),
            ],
        ),
    ]