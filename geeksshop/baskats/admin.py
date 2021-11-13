from django.contrib import admin

# Register your models here.
from baskats.models import Basket


@admin.register(Basket)
class BasketAdmin(admin.ModelAdmin):
    list_display = ('user', 'products', 'quantity',) #порядок отображения полей в таблице admin
    list_display_links = ('user',)