from django.db import models


class CategoryProducts(models.Model):
    name = models.CharField(max_length=50, unique=True, name='category_name')
    description = models.TextField(max_length=200, blank= True, name='category_description')

    def __str__(self):
        return self.category_name

class Products(models.Model):
    name = models.CharField(max_length=50, name='products_name')
    description = models.TextField(max_length=200, blank=True, name='products_descriptions')
    price = models.DecimalField(max_digits=10, decimal_places=2, name='products_price')
    image = models.ImageField(upload_to='products_image', blank=True)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(CategoryProducts, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.products_name}'


# Create your models here.
