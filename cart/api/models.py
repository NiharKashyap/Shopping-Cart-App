from django.db import models

# Create your models here.
class ShoppingCart(models.Model):
    user = models.PositiveIntegerField()
    item = models.CharField(max_length=10)
    quantity = models.PositiveIntegerField()
    
    def __str__(self):
        rep = f"User {self.user} Item {self.item}"
        return rep