from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'products/index.html', {
        'page_name': 'GeekShop Store',
        'title': 'GeekShop',
        'content': 'Новые образы и лучшие бренды на GeekShop Store.\
                    Бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям.'
        })

def products(request):
    return render(request, 'products/products.html', 
        {
            'items':[
                    {'url': 'vendor/img/products/Adidas-hoodie.png',
                    'title': 'Худи черного цвета с монограммами adidas Originals',
                    'price': '6 090,00 руб.',
                    'content': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'},
                    {'url': 'vendor/img/products/Blue-jacket-The-North-Face.png',
                    'title': 'Синяя куртка The North Face',
                    'price': '23 725,00 руб.',
                    'content': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'},
                    {'url': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
                    'title': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                    'price': '3 390,00 руб.',
                    'content': 'Материал с плюшевой текстурой. Удобный и мягкий.'},
                    {'url': 'vendor/img/products/Black-Nike-Heritage-backpack.png',
                    'title': 'Черный рюкзак Nike Heritage',
                    'price': '2 340,00 руб.',
                    'content': 'Плотная ткань. Легкий материал.'},
                    {'url': 'vendor/img/products/Black-Dr-Martens-shoes.png',
                    'title': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
                    'price': '13 590,00 руб.',
                    'content': 'Гладкий кожаный верх. Натуральный материал.'},
                    {'url': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
                    'title': 'Темно-синие широкие строгие брюки ASOS DESIGN',
                    'price': '2 890,00 руб.',
                    'content': 'Легкая эластичная ткань сирсакер Фактурная ткань.'}],
                    'title': 'GeekShop - Каталог',
                })