from django.urls import reverse
from rest_framework import status
from rest_framework.authtoken.admin import User
from rest_framework.test import APITestCase
from ludzie.models import Stanowisko


class AccountTests(APITestCase):
    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        user = User.objects.create_user('testUser', 'email@example.com', 'password')
        url = reverse('account-list')
        data = {'name': 'DabApps'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Account.objects.count(), 1)
        self.assertEqual(Account.objects.get().name, 'DabApps')

    def setUp(self):
        self.team = Team.objects.create(name='Loosers', country='PL')
        self.user = User.objects.create_user(username='testuser', password='12345')
        client.force_authenticate(user=self.user)
        self.zbyszek = Person.objects.create(
            name='Zbyszek', shirt_size='L', miesiac_dodania=1, team=self.team)

    def test_get_valid_single_person(self):
        request = client.get(f'/ankiety/persons/{self.zbyszek.pk}/')
        person = Person.objects.get(pk=self.zbyszek.pk)
        serializer = PersonSerializer(person)
        response = request.render()
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)