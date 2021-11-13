from django.db import models

# Create your models here.
from django.db.models.signals import pre_delete, pre_save
from django.dispatch import receiver

from geeksshop import settings
from products.models import Products

from baskats.models import Basket


class Order(models.Model):

    FORMING = 'FM'
    SEND_TO_PROCEED = 'STP'
    PAID = 'PD'
    PROCEEDED = 'PRO'
    READY = 'RDY'
    CANCEL = 'CNC'

    ORDER_STATUS_CHOICES = (
        (FORMING, 'формируется'),
        (SEND_TO_PROCEED, 'отправлен в обработку'),
        (PAID, 'оплачено'),
        (PROCEEDED, 'обрабатывается'),
        (READY, 'готову выдаче'),
        (CANCEL, 'отмена заказа'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(verbose_name='создан', auto_now_add=True)
    update = models.DateTimeField(verbose_name='обновлен', auto_now=True)
    status = models.CharField(choices=ORDER_STATUS_CHOICES, verbose_name='статус', max_length=3, default=FORMING)
    is_active = models.BooleanField(verbose_name='активный', default=True)

    def __str__(self):
        return f'Текущий заказ {self.pk}'

    def get_total_quantity(self):
        items = self.order_items.select_related()
        return sum(list(map(lambda x: x.quantity, items)))

    def get_total_cost(self):
        items = self.order_items.select_related()
        # print(self.order_items)
        return sum(list(map(lambda x: x.get_product_cost(), items)))

    def get_items(self):
        pass

    def delete(self, using=None, keep_parents=False, num=None):

        for item in self.order_items.select_related():
            item.products.quantity += item.quantity

            item.save()
        self.is_active = True
        self.save()

        def get_summary(self):
            items = self.order_items.select_related()
            return {
            'get_total_cost': sum(list(map(lambda x: x.get_product_cost(), items))),
            'get_total_quantity': sum(list(map(lambda x: x.quantity, items)))}

class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    product = models.ForeignKey(Products, verbose_name='продукты', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)


    def get_product_cost(self):
        return self.product.products_price * self.quantity

    @staticmethod
    def get_item(pk):
        return OrderItem.objects.get(pk=pk).quantity

@receiver(pre_delete, sender=Basket)
@receiver(pre_delete, sender=OrderItem)
def product_quantity_update_delete(sender, instance, **kwargs):
    instance.product.quantity += instance.quantity
    instance.save()


@receiver(pre_save, sender=Basket)
@receiver(pre_save, sender=OrderItem)
def product_quantity_update_delete(sender, instance, **kwargs):
    if instance.pk:
        # print(1, instance, type(instance))
        instance.product.quantity = instance.quantity - instance.get_item(int(instance.pk))
        instance.product.save()
    else:
        # print(2)
        instance.products.quantity -= instance.quantity
        instance.products.save()