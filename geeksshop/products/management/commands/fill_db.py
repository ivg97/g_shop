
import json
from django.core.management.base import BaseCommand


from geeksshop.products.models import CategoryProducts, Products

JSON_PATH = 'products/fixtures'

def load_from_json(file_name):
    with open(file_name, mode='r', encoding='utf-8') as infile:

        return json.load(infile)


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = load_from_json('category.json')

        CategoryProducts.objects.all().delete()
        for category in categories:
            cat = category.get('fields')
            cat['id'] = category.get('pk')
            new_category = CategoryProducts(**cat)
            new_category.save()

        products = load_from_json('products.json')

        Products.objects.all().delete()
        for product in products:
            prod = product.get('fields')
            category = prod.get('category')
            _category = CategoryProducts.objects.get(id=category)
            prod['category'] = _category
            new_category = Products(**prod)
            new_category.save()