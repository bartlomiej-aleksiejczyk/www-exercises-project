from rest_framework import status
from rest_framework.authtoken.admin import User
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from ludzie.models import Stanowisko


class StanowiskoTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        Stanowisko.objects.create(nazwa='Tester ', opis='testuje aplikacje')
        self.token = Token.objects.get(user=self.user)


    def test_endpoint_with_token_auth(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        response = self.client.get('http://127.0.0.1:8000/ludzie/stanowisko/1/members/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)