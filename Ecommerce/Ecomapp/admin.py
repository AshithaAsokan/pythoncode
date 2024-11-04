from django.contrib import admin
from .models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display=['id','name','price','brand','description']
    ordering=('name',)
    search_fields=('name','brand')

admin.site.register(Product,ProductAdmin) 