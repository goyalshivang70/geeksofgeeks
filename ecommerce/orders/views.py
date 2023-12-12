from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Order, OrderItem, Product
from .serializers import OrderSerializer, OrderItemSerializer, ProductSerializer, PlaceOrderSerializer

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

class OrderListView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)

class OrderItemListView(generics.ListAPIView):
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        order_id = self.kwargs['order_id']
        return OrderItem.objects.filter(order__id=order_id)

class PlaceOrderView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity')
        # Validate the parameters
        if not product_id or not quantity:
            return Response({'error': 'Product and Quantity are required.'}, status=status.HTTP_400_BAD_REQUEST)
        # Create Order
        order = Order.objects.create(user=request.user)
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            return  Response({'error': f"Product with id {product_id} does not exist."})
        # Create Order Item
        OrderItem.objects.create(order=order, product=product, quantity=quantity)
        # Serialize the order for the response
        order_serializer = OrderSerializer(order)
        return Response(order_serializer.data, status=status.HTTP_201_CREATED)
