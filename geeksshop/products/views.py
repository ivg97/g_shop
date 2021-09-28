from django.shortcuts import render
from django.conf import settings

from .models import Products


def index(request):
    return render(request, 'products/index.html', {
        'page_name': 'GeekShop Store',
        'title': 'GeekShop',
        'content': 'Новые образы и лучшие бренды на GeekShop Store.\
                    Бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям.'
    })


def products(request):
    products = Products.objects.all()
    media = settings.MEDIA_URL
    return render(request, 'products/products.html', {'products': products,
                                                      'media': media})
