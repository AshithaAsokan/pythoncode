from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)  # Increased length for product name
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Using DecimalField for price
    brand = models.CharField(max_length=50)  # Increased length for brand name
    description = models.CharField(max_length=255)  # Increased length for description

    def __str__(self):
        return f"{self.name} by {self.brand} - ${self.price}"

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name} for {self.user.username}"

class Order(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ordered_at = models.DateTimeField(auto_now_add=True)
    order_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')  # New status field

    def __str__(self):
        return f"Order #{self.id} by {self.user.username} - {self.order_status}"
