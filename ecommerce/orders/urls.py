from django.urls import path
from .views import OrderListView, OrderItemListView, ProductListView, PlaceOrderView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('order-items/<int:order_id>/', OrderItemListView.as_view(), name='order-item-list'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('place-order/', PlaceOrderView.as_view(), name='place-order'),
]
