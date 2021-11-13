from django.db import models


class CategoryProducts(models.Model):
    name = models.CharField(max_length=50, unique=True, name='category_name')
    description = models.TextField(max_length=200, blank= True, name='category_description')
    active = models.BooleanField(default=True, name='active')
    discont = models.PositiveIntegerField(default=0, name='discont')

    def __str__(self):
        return self.category_name

class Products(models.Model):
    name = models.CharField(max_length=50, name='products_name')
    description = models.TextField(max_length=200, blank=True, name='products_descriptions')
    price = models.DecimalField(max_digits=10, decimal_places=2, name='products_price')
    image = models.ImageField(upload_to='products_image', blank=True)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(CategoryProducts, on_delete=models.CASCADE)
    active = models.BooleanField(default=True, name='active')
    sale = models.PositiveIntegerField(default=0, name='sale')

    # def __init__(self, *args, **kwargs):
    #     super(Products, self).__init__(*args, **kwargs)
    #     if self.category.discont and self.sale:
    #         pass
            # self.products_price = self.total_price()
            # self.save()

    def __str__(self):
        return f'{self.products_name}'

    def total_sale(self):
        return self.sale + self.category.discont

    def total_price(self):
        if self.total_sale():
            return self.products_price - ((self.products_price / 100) * self.total_sale())
        else:
            return self.products_price



# Create your models here.
