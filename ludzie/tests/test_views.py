from django.test import RequestFactory, TestCase
from django.urls import reverse

from ludzie.views import home_view

class ViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_home_view(self):
        request = self.factory.get(reverse("home"))
        response = home_view(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.template_name, "home.html")
