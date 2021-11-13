from django.conf import settings
from django.test import TestCase
from django.test.client import Client

# Create your tests here.
from products.models import CategoryProducts, Products
from users.models import User


class TestUser(TestCase):
    status_code_success = 200
    status_code_render = 302
    username = 'ivg'
    email = 'ivg@mail.ru'
    password = '1'

    new_user_data = {
        'username':'ivg_97.97',
        'first_name':'ivan',
        'last_name': 'ivan',
        'password1': '1234qwert',
        'password2': '1234qwert',
        'email': 'qwert@mail.ru',

    }


    def setUp(self) -> None:
        self.user = User.objects.create_superuser(self.username,email=self.email,password=self.password)
        self.client = Client()


    def test_login(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code,self.status_code_success)
        self.assertTrue(response.context['user'].is_anonymous)
        self.client.login(username=self.username,password=self.password)
        response = self.client.get('/users/login/')
        self.assertEqual(response.status_code, self.status_code_success)

    def test_register(self):
        response = self.client.post('/users/register/',data=self.new_user_data)
        self.assertEqual(response.status_code,self.status_code_render)
        new_user = User.objects.get(username=self.new_user_data['username'])
        activation_url = f"{settings.DOMAIN_NAME}/users/verify/{self.new_user_data['email']}/{new_user.activation_key}/"
        response = self.client.get(activation_url)
        self.assertEqual(response.status_code, self.status_code_render)
        # new_user.refresh_from_db()
        # self.assertTrue(new_user.is_active)

