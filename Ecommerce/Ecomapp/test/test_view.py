
from django.test import TestCase,Client
from django.urls import reverse
from Ecomapp.models import Product

class Testviews(TestCase):
   def testviewshome(self):
      client=Client()
      response=client.get(reverse('home'))
      self.assertEquals(response.status_code,200)
         self.assertTemplateUsed(response,'index.html')