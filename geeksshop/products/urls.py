from django.urls import path



from .views import index, products

app_name = 'products'

urlpatterns = [
    path('', products, name='products_url'),
    path('category/<int:category_id>/', products, name='category'),
    path('page/<int:page_id>/', products, name='page'),
]
