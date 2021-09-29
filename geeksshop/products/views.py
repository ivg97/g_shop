from django.shortcuts import render


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
    return render(request, 'products/products.html', {'products': products})
