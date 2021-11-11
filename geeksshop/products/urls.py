from django.urls import path



from .views import index, products, ProductDetail

app_name = 'products'

urlpatterns = [
    path('', products, name='products_url'),
    path('category/<int:category_id>/', products, name='category'),
    path('page/<int:page_id>/', products, name='page'),
    path('product/<int:pk>/<int:cat>', ProductDetail.as_view(), name='product_detail'),
]
