
from django.urls import path, include
from .views import OrderList, OrderCreate, OrderDelete, OrderDetail, OrderUpdate, order_forming_complete, add_pro


app_name = 'orders'

urlpatterns = [
    path('', OrderList.as_view(), name='list'),
    path('create/', OrderCreate.as_view(), name='create'),
    path('update/<int:pk>/', OrderUpdate.as_view(), name='update'),
    path('read/<int:pk>/', OrderDetail.as_view(), name='read'),
    path('delete/<int:pk>/', OrderDelete.as_view(), name='delete'),
    path('forming_complete/<int:pk>/', order_forming_complete, name='forming_complete'),
    path('add_pro/<int:id>/', add_pro, name='add_pro'),

]