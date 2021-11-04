from django.db import models
from django.utils.functional import cached_property

from users.models import User
from products.models import Products

# class BasketsQuerySet(models.QuerySet):
#
#     def delete(self, *args, **kwargs):
#         for item in self:
#             item.products.quantity += item.quantity
#             item.products.save()
#         super(BasketsQuerySet, self).delete()



class Basket(models.Model):
    # objects = BasketsQuerySet.as_manager()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='basket')
    products = models.ForeignKey(Products, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    created_timestamp = models.DateTimeField(auto_now_add=True)
    update_timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Корзина для {self.user.username} | Продукт {self.products.products_name}'

    def sum(self):
        return self.quantity * self.products.products_price

    def total_quantity(self):
        # baskets = Basket.objects.filter(user=self.user)
        baskets = self.get_item_cached
        total = 0
        for basket in baskets:
            total += basket.quantity
        return total

    def total_sum(self):
        # baskets = Basket.objects.filter(user=self.user)
        baskets = self.get_item_cached
        sum = 0
        for basket in baskets:
            sum += basket.sum()
        return sum
    
    # def delete(self, using=None, keep_parents=False):
    #     self.products.quantity += self.quantity
    #     self.products.save()
    #     super(Basket, self).delete()
    #
    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     print(1)
    #     if self.pk:
    #         print(2)
    #         self.products.quantity += self.quantity - self.get_item(int(self.pk))
    #     else:
    #         print(3)
    #         self.products.quantity -= self.quantity
    #     self.products.save()
    #     super(Basket, self).save()


    @staticmethod
    def get_item(pk):
        return Basket.objects.get(pk=pk).quantity


    @cached_property
    def get_item_cached(self):
        return self.user.basket.select_related()
