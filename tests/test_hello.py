from django.test import TestCase
from django.urls import reverse


class TestClass(TestCase):
    def test_hello(self):
        url = reverse("h")
        response = self.client.get(url)
        assert response.status_code == 200
