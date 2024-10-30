from django.contrib.auth.models import User
from django.views.decorators.cache import cache_page
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from .models import Order, OrderItem
from .models import DeliveryAddress
from rest_framework.permissions import IsAuthenticated
from .serializers import OrderSerializer, OrderItemSerializer
from .serializers import DeliveryAddressSerializer
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework import status
from .tasks import send_welcome_email

# перехват ошибки через Sentry
class TriggerErrorView(APIView):
    def get(self, request):
        # Создаем исключение для тестирования
        division_by_zero = 1 / 0
        return Response({"message": "This won't be reached."}, status=status.HTTP_200_OK)


# Регистрация
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    # тут добавил celery-задачу
    def perform_create(self, serializer):
        user = serializer.save()
        # отправка приветственного письма асинхронно
        send_welcome_email.delay(user.email)

class LoginView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]


class ProductListView(generics.ListAPIView):
    @cache_page(60 * 15)
    def get(self, request):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer
        return Response(serializer_class.data)

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'id'

class AddToCartView(generics.CreateAPIView):
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        order, created = Order.objects.get_or_create(user=self.request.user, status='pending')
        serializer.save(order=order)

class RemoveFromCartView(generics.DestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = [IsAuthenticated]

class DeliveryAddressCreateView(generics.CreateAPIView):
    queryset = DeliveryAddress.objects.all()
    serializer_class = DeliveryAddressSerializer
    permission_classes = [IsAuthenticated]

class DeliveryAddressDeleteView(generics.DestroyAPIView):
    queryset = DeliveryAddress.objects.all()
    serializer_class = DeliveryAddressSerializer
    permission_classes = [IsAuthenticated]

class OrderListView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


class OrderStatusUpdateView(APIView):
    def patch(self, request, order_id):
        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return JsonResponse({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_200_OK)

        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)