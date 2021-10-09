from django.db import models

from users.models import User
from products.models import Products



class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    update_timestamp = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.products.products_name}'

    def sum(self):
        return self.quantity * self.products.products_price

    def total_quantity(self):
        baskets = Basket.objects.filter(user=self.user)
        total = 0
        for basket in baskets:
            total += basket.quantity
        return total

    def total_sum(self):
        baskets = Basket.objects.filter(user=self.user)
        sum = 0
        for basket in baskets:
            sum += basket.sum()
        return sum