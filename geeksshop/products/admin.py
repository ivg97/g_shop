from django.contrib import admin
from .models import CategoryProducts, Products
# Register your models here.


@admin.register(CategoryProducts)
class CategoryProductsAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'category_description') #порядок отображения полей в таблице admin
    list_display_links = ('category_name',)




@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('products_name', 'category', 'products_price', 'quantity', 'image', 'products_descriptions', )
    fields = ('products_name', 'image', 'products_descriptions', 'products_price', 'quantity', 'category')
    list_display_links = ('products_name',)
    readonly_fields = ('products_descriptions',) # только на чтение
    ordering = ('products_price',)
    search_fields = ('products_name',)



