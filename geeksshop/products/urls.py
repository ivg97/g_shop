from django.urls import path
from .views import index, products

name_app = 'products'

urlpatterns = [
    path('', index, name='index'),
    path('products/', products, name='products'),
]
