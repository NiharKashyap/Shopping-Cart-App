from dataclasses import field
from .models import ShoppingCart
from rest_framework.serializers import ModelSerializer

class CartSerializer(ModelSerializer):
    class Meta:
        model=ShoppingCart
        fields='__all__'
        # fields = ('item', 'quantity')

