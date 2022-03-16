from django.db import models

# Create your models here.
class ShoppingCart(models.Model):
    user = models.PositiveIntegerField()
    item = models.CharField(max_length=10)
    quantity = models.PositiveIntegerField()