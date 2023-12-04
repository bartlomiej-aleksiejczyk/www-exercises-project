from django.test import RequestFactory, TestCase
from django.urls import reverse

from ludzie.views import osoba_list

class Osoba_listTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_home_view(self):
        request = self.factory.get(reverse("osoba_list"))
        response = osoba_list(request)
        self.assertEqual(response.status_code, 200)
