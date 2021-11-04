from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DetailView

from .models import Products, CategoryProducts
from django.conf import settings
from django.core.cache import cache


def index(request):
    context = {
        'page_name': 'GeekShop Store',
        'title': 'GeekShop',
        'content': 'Новые образы и лучшие бренды на GeekShop Store.\
                    Бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям.'
    }
    return render(request, 'products/index.html', context)

def get_links_category():
    if settings.LOW_CACHE:
        key = 'links_category'
        link_category = cache.get(key)
        if link_category is None:
            link_category = CategoryProducts.objects.all()
            cache.set(key, link_category)
        return link_category
    else:
        return CategoryProducts.objects.all()

def get_product(id):
    if settings.LOW_CACHE:
        key = f'product{id}'
        product = cache.get(key)
        if product is None:
            product = get_object_or_404(Products, pk=id)
            cache.set(key, product)
        return product
    else:
        return get_object_or_404(Products, pk=id)


def products(request, category_id=None, page_id=1):
    if category_id == None:
        products = Products.objects.filter(active=True)
    else:
        products =Products.objects.filter(category_id=category_id).filter(active=True)

    paginator = Paginator(products, per_page=5)
    try:
        products_paginator = paginator.page(page_id)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context = {'products': products,
               'categories': CategoryProducts.objects.filter(active=True),
               # 'categories': get_links_category(),
               'title': 'Каталог'}
    context.update({'products': products_paginator})
    return render(request, 'products/products.html', context)


class ProductDetail(DetailView):
    model = Products
    template_name = 'products/product_detail.html'
    context_object_name = 'product'


    def get_context_data(self, category_id=None, *args, **kwargs):
        context = super().get_context_data()

        context['product'] = get_product(self.kwargs.get('pk'))
        context['categories'] = CategoryProducts.objects.all()
        return context