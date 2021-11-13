from django.test import TestCase
from products.models import CategoryProducts, Products
from django.test.client import Client


class TestMainSmokeTest(TestCase):

    def setUp(self):
        category = CategoryProducts.objects.create(
            name='Test1'
        )
        Products.objects.create(
            category=category,
            name='product_test_1',
            price=100
        )
        self.client = Client()


    def test_products_pages(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_products_product(self):
        for product_item in Products.objects.all():
            response = self.client.get(f'/products/detail/{product_item.pk}/')
            self.assertEqual(response.status_code, 200)