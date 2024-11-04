from django.test import TestCase
from Ecomapp.models import Product

class TestModel(TestCase):
    def testmodelproduct(self):
        pdt=Product.objects.create(name="car",price="500000")
        self.assertIsInstance(pdt,Product)