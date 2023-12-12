# api/serializers.py

from rest_framework import serializers
from .models import Order, OrderItem, Product
from django.db.models import Sum

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'description']

class OrderItemSerializer(serializers.ModelSerializer):
    product = serializers.CharField(source='product.name')

    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'item_price']

class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = ['id', 'user', 'total_price', 'created_at']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        total_price = total_price = OrderItem.objects.filter(order=instance).aggregate(Sum('item_price'))['item_price__sum']
        data['total_price'] = total_price or 0
        return data


class PlaceOrderSerializer(serializers.Serializer):
    products = serializers.ListField(child=serializers.IntegerField())
    quantities = serializers.ListField(child=serializers.IntegerField())