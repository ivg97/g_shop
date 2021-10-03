from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import render

from users.models import User

from admins.forms import UserAdminRegisterForm, UserAdminProfileForm, CategoryCreateForm

from geeksshop.mixin import CustomDispatchMixin

from products.models import CategoryProducts


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


def category_list_view(request):
    categories = CategoryProducts.objects.all()
    context = {'categories': categories,
               'title': 'Админка | Категории продуктов'}
    return render(request, 'admins/categories-read.html', context)


def category_create(request):
    if request.method == 'POST':
        form = CategoryCreateForm(data=request.POST)
        if form.is_valid():
            name = request.POST['category_name']
            descriptions = request.POST['category_description']
            category = CategoryProducts.objects.create(category_name=name, category_description=descriptions)
            category.save()
            return HttpResponseRedirect(reverse('admins:category_list_view'))
    else:
        form = CategoryCreateForm()

    context = {'title': 'Админка | Создание категории',
               'form': form}
    return render(request, 'admins/category_create.html', context)


def category_update(request, pk):
    category = CategoryProducts.objects.get(id=pk)
    context = {'category': category}
    return render(request, 'admins/category-update-delete.html', context)


def category_delete(request, id):
    pass
