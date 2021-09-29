from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import UserLoginForms, UserRegisterForms, UserProfileForm
from baskats.models import Basket


def login(request):

    if request.method == 'POST':
        form = UserLoginForms(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse('index'))
    else:
        form = UserLoginForms()
    context = {
        'title': 'Geekshop - Авторизация',
        'form': form
    }
    return render(request, 'users/login.html', context)

@login_required
def register(request):
    if request.method == 'POST':
        form = UserRegisterForms(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Вы успешно зарегистрировались!')
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegisterForms()


    context = {
        'title': 'Geekshop - Регистрация',
        'form': form,

    }

    return render(request, 'users/register.html', context)


def profile(request):

    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, instance=request.user, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Изменения сохранены!')
            return HttpResponseRedirect(reverse('users:profile'))
        else:
            print(form.errors)
            # print(messages)


    context = {
        'title': 'Geekshop - Профиль',
        'form': UserProfileForm(instance=request.user),
        'baskets': Basket.objects.filter(user=request.user)
    }
    return render(request, 'users/profile.html', context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))



