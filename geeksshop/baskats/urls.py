from django.urls import path


from .views import basket_add, basket_remote, basket_edit


app_name = 'baskets'

urlpatterns = [
    path('add/<int:product_id>/', basket_add, name='basket_add'),
    path('remove/<int:product_id>/', basket_remote, name='basket_remote'),
    path('edit/<int:id>/<int:quantity>/', basket_edit, name='basket_edit'),
]
