from django.urls import path


from .views import basket_add, basket_remote


app_name = 'baskets'

urlpatterns = [
    path('add/<int:product_id>/', basket_add, name='basket_add'),
    path('remove/<int:product_id>/', basket_remote, name='basket_remote'),
]
