from django.db.models import Q
from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import DetailView

from .models import Products, CategoryProducts


def index(request):
    context = {
        'page_name': 'GeekShop Store',
        'title': 'GeekShop',
        'content': 'Новые образы и лучшие бренды на GeekShop Store.\
                    Бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям.'
    }
    return render(request, 'products/index.html', context)


def products(request, category_id=None, page_id=1):
    if category_id == None:
        products = Products.objects.filter(active=True)
    else:
        products =Products.objects.filter( Q(category_id=category_id) & Q(active=True))

    paginator = Paginator(products, per_page=6)
    try:
        products_paginator = paginator.page(page_id)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)

    context = {'products': products,
               'categories': CategoryProducts.objects.filter(active=True),
               'title': 'Каталог'}
    context.update({'products': products_paginator})
    return render(request, 'products/products.html', context)



class ProductDetail(DetailView):
    model = Products
    template_name = 'products/product_detail.html'
    context_object_name = 'product'


    def get_context_data(self, category_id=None, *args, **kwargs):
        context = super().get_context_data()

        context['product'] = Products.objects.get(pk=self.kwargs.get('pk'))
        context['categories'] = CategoryProducts.objects.all()
        context['recomm'] = Products.objects.filter(category_id=self.kwargs.get('cat'))
        return context
