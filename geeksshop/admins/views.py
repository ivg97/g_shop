from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render

from users.models import User
from admins.forms import UserAdminRegisterForm, UserAdminProfileForm, CategoryCreateForm, ProductsCreateForm
from geeksshop.mixin import CustomDispatchMixin
from products.models import CategoryProducts, Products


def index(request):
    return render(request, 'admins/admin.html')


class UserListView(ListView, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-read.html'
    context_object_name = 'users'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Пользователи'
        return context


class UserCreateView(CreateView, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-create.html'
    form_class = UserAdminRegisterForm
    success_url = reverse_lazy('admins:admins_user')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Регистрация'
        return context




class UserUpdateView(UpdateView, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    form_class = UserAdminProfileForm
    success_url = reverse_lazy('admins:admins_user')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Обновление пользователя'
        return context


class UserDeleteView(DeleteView, CustomDispatchMixin):
    model = User
    template_name = 'admins/admin-users-read.html'
    success_url = reverse_lazy('admins:admins_user')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, request, *args, **kwargs):
        return super(UserDeleteView, self).dispatch(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object.is_active:
            self.object.is_active = False
            self.object.save()
        else:
            self.object.is_active = True
            self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class CategoryListView(ListView, CustomDispatchMixin):
    model = CategoryProducts
    template_name = 'admins/categories-read.html'
    context_object_name = 'categories'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Категории'
        return context


class CategoryCreateView(CreateView, CustomDispatchMixin):
    model = CategoryProducts
    template_name = 'admins/category_create.html'
    form_class = CategoryCreateForm
    success_url = reverse_lazy('admins:category_list_view')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Создание категории'
        return context


class CategoryUpdateView(UpdateView, CustomDispatchMixin):
    model = CategoryProducts
    template_name = 'admins/category-update-delete.html'
    form_class = CategoryCreateForm
    success_url = reverse_lazy('admins:category_list_view')
    context_object_name = 'categories'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryUpdateView, self).get_context_data(**kwargs)
        context['title'] = f'Админка | Редактирование категории | {self.object}'
        return context


class CategoryDeleteView(DeleteView, CustomDispatchMixin):
    model = CategoryProducts
    template_name = 'admins/category-update-delete.html'
    success_url = reverse_lazy('admins:category_list_view')



class ProductsAdminListView(ListView, CustomDispatchMixin):
    model = Products
    template_name = 'admins/products-list-view.html'
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsAdminListView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Продукты'
        return context


class ProductsAdminCreateView(CreateView, CustomDispatchMixin):
    model = Products
    template_name = 'admins/products-create.html'
    form_class = ProductsCreateForm
    success_url = reverse_lazy('admins:products_list_view')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsAdminCreateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка | Добавление продукта'
        return context

class ProductsAdminUpdateView(UpdateView, CustomDispatchMixin):
    model = Products
    template_name = 'admins/products-update-delete.html'
    form_class = ProductsCreateForm
    success_url = reverse_lazy('admins:products_list_view')
    context_object_name = 'products'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductsAdminUpdateView, self).get_context_data(**kwargs)
        context['title'] = f'Админка | Редактирование продукта | {self.object}'
        return context

class ProductsAdminDeleteView(DeleteView, CustomDispatchMixin):
    model = Products
    template_name = 'admins/products-update-delete.html'
    success_url = reverse_lazy('admins:products_list_view')