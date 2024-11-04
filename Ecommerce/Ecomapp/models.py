from django.db import models

# Create your models here.
class Product(models.Model):
    name= models.CharField(max_length=10)
    price= models.IntegerField()
    brand= models.CharField(max_length=10)
    description= models.CharField(max_length=30)