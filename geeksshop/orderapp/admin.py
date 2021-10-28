from django.contrib import admin
from .models import Order, OrderItem
# Register your models here.

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'created', 'update', 'status', 'is_active', )
    list_display_links = ('id',)
    # readonly_fields = ('products_descriptions',) # только на чтение
    # ordering = ('products_price',)
    # search_fields = ('products_name',)

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity',)
    list_display_links = ('order',)