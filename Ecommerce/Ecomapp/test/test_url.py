
from django.test import SimpleTestCase
from django.urls import reverse,resolve
from Ecomapp.views import home

class TestUrl(SimpleTestCase):
    def test_home(self):
        url=reverse('home')
        print(resolve(url))
        self.assertEqual(resolve(url).func,home)