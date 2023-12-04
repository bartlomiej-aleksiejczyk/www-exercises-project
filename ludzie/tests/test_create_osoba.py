
from rest_framework import status
from rest_framework.authtoken.admin import User
from rest_framework.test import APITestCase

from ludzie.models import Stanowisko


class OsobaTest(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='bartek', password='bartek')
        Stanowisko.objects.create(nazwa='Tester ', opis='testuje aplikacje')

    def test_endpoint_with_password_auth(self):
        login = self.client.login(username='bartek', password='bartek')
        self.assertTrue(login)
        post_data = {
            "imie": "Jan",
            "nazwisko": "Kowalski",
            "plec": 2,
            "stanowisko": 1
        }
        response = self.client.post('http://127.0.0.1:8000/ludzie/osoba/create/',
                                    post_data,
                                    content_type='application/json')
        print(response)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.client.logout()
