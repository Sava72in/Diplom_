# создал файл с тестами для views.py
# тесты сгенерированы через чат GPT, как указывалось в правках
# впишите в консоль:
# ------------------------
# coverage run -m pytest |
# coverage report -m     |
# ------------------------


import pytest
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Product, OrderItem, Order


@pytest.fixture
def api_client():
    return APIClient()


@pytest.mark.django_db
def test_register_user(api_client):
    url = reverse('register')
    data = {'username': 'testuser', 'password': 'testpassword', 'email': 'qwerty@gmail.com'}
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    assert User.objects.filter(username='testuser').exists()


@pytest.mark.django_db
def test_login_user(api_client):
    # Создаем тестового пользователя
    User.objects.create_user(username='testuser', password='testpassword')
    url = reverse('token_obtain_pair')
    data = {'username': 'testuser', 'password': 'testpassword'}
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_200_OK
    assert 'access' in response.data


@pytest.mark.django_db
def test_get_product_list(api_client):
    # Создаем тестовый продукт
    Product.objects.create(name='Test Product', price=10.0, description='Test Description')
    url = reverse('product-list')
    response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 1


@pytest.mark.django_db
def test_add_to_cart(api_client):
    # Создаем тестового пользователя и продукт
    user = User.objects.create_user(username='testuser', password='testpassword')
    product = Product.objects.create(name='Test Product', price=10.0, description='Test Description')

    # Аутентифицируем пользователя
    api_client.force_authenticate(user=user)
    url = reverse('add-to-cart')
    data = {'product_id': product.id, 'quantity': 1}
    response = api_client.post(url, data)
    assert response.status_code == status.HTTP_201_CREATED
    assert OrderItem.objects.filter(order__user=user, product=product).exists()