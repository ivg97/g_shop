from django.urls import path

from .views import index, UserListView, UserUpdateView, UserCreateView, UserDeleteView, category_list_view, category_create, category_update, category_delete


app_name = 'admins'

urlpatterns = [
    path('', index, name='index'),
    path('users/', UserListView.as_view(), name='admins_user'),
    path('users-create/', UserCreateView.as_view(), name='admins_user_create'),
    path('users-update/<int:pk>/', UserUpdateView.as_view(), name='admins_user_update'),
    path('users-delete/<int:pk>', UserDeleteView.as_view(), name='admins_user_delete'),
    path('categories/', category_list_view, name='category_list_view'),
    path('category-create/', category_create, name='category_create'),
    path('category-update/<int:pk>/', category_update, name='category_update'),
    path('category-delete/<int:pk>/', category_delete, name='category_delete'),

]
