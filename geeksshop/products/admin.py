from django.contrib import admin
from .models import CategoryProducts, Products
# Register your models here.


@admin.register(CategoryProducts)
class CategoryProductsAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'category_description')
    list_display_links = ('category_name',)




@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('products_name', 'category', 'products_price', 'quantity', 'image', 'products_descriptions', )
    list_display_links = ('products_name',)



