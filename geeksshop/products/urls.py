from django.urls import path
from django.views.decorators.cache import cache_page

from .views import index, products, ProductDetail

app_name = 'products'

urlpatterns = [
    path('', products, name='products_url'),
    path('category/<int:category_id>/', cache_page(3600)(products), name='category'),
    path('page/<int:page_id>/', cache_page(3600)(products), name='page'),
    path('detail/<int:pk>/', cache_page(3600)(ProductDetail.as_view()), name='detail'),
]
