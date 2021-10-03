from django.shortcuts import render


from .models import Products, CategoryProducts


def index(request):
    context = {
        'page_name': 'GeekShop Store',
        'title': 'GeekShop',
        'content': 'Новые образы и лучшие бренды на GeekShop Store.\
                    Бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям.'
    }
    return render(request, 'products/index.html', context)


def products(request):
    products = Products.objects.all()
    categories = CategoryProducts.objects.all()
    context = {'products': products,
               'categories': categories}
    return render(request, 'products/products.html', context)
