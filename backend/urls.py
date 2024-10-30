from django.urls import path
from .views import RegisterView, LoginView
from .views import ProductListView
from .views import ProductDetailView
from .views import AddToCartView, RemoveFromCartView
from .views import DeliveryAddressCreateView, DeliveryAddressDeleteView, OrderListView, OrderDetailView, OrderStatusUpdateView
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView
)

from .views import TriggerErrorView
from . import views




urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('products/<int:id>/', ProductDetailView.as_view(), name='product-detail'),
    path('cart/remove/<int:pk>/', RemoveFromCartView.as_view(), name='remove-from-cart'),
    path('cart/add/', AddToCartView.as_view(), name='add-to-cart'),
    path('delivery-address/', DeliveryAddressCreateView.as_view(), name='delivery-address-create'),
    path('delivery-address/<int:pk>/', DeliveryAddressDeleteView.as_view(), name='delivery-address-delete'),
    path('orders/', OrderListView.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('orders/<int:pk>/status/', OrderStatusUpdateView.as_view(), name='order-status-update'),
    # схема
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    # Swagger UI
    path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # Redoc
    path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('trigger-error/', TriggerErrorView.as_view(), name='trigger-error'),
]
# после запуска сервера перейдите на страницу
# http://127.0.0.1:8000/api/docs/ для
# просмотра автосгенерированной документации Swagger,