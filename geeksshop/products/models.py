from django.db import models


class CategoryProducts(models.Model):
    name = models.CharField(max_length=50, unique=True, name='category_name')
    description = models.TextField(max_length=200, blank= True, name='category_description')


class Products(models.Model):
    name = models.CharField(max_length=50, name='products_name')
    description = models.TextField(max_length=200, blank=True, name='products_descriptions')
    price = models.DecimalField(max_digits=5, decimal_places=2, name='products_price')
    image = models.ImageField(upload_to='products_image', blank=True)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(CategoryProducts, on_delete=models.CASCADE)



# Create your models here.
