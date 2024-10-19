from django.contrib.auth.models import User
from django.db import models

# Модель для магазина
class Shop(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
        return self.name

# Модель для категории товаров
class Category(models.Model):
    shops = models.ManyToManyField(Shop, related_name='categories')
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Модель для продукта
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Модель для информации о продукте
class ProductInfo(models.Model):
    product = models.ForeignKey(Product, related_name='product_info', on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, related_name='product_info', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_rrc = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} - {self.shop.name}"

# Модель для параметра товара (например, размер, цвет и т.д.)
class Parameter(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# Модель для связи между информацией о продукте и его параметрами
class ProductParameter(models.Model):
    product_info = models.ForeignKey(ProductInfo, related_name='parameters', on_delete=models.CASCADE)
    parameter = models.ForeignKey(Parameter, related_name='product_parameters', on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.parameter.name}: {self.value}"

# Модель для заказа
class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    dt = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Pending')

    def __str__(self):
        return f"Order #{self.id} - {self.status}"

# Модель для элементов заказа (каждый товар в заказе)
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    shop = models.ForeignKey(Shop, related_name='order_items', on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.product.name} - {self.quantity}"

# Модель для контактов пользователя (например, email, телефон)
class Contact(models.Model):
    CONTACT_TYPES = [
        ('email', 'Email'),
        ('phone', 'Phone'),
    ]
    type = models.CharField(max_length=10, choices=CONTACT_TYPES)
    user = models.ForeignKey(User, related_name='contacts', on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.type}: {self.value}"

class DeliveryAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address_line = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.address_line}, {self.city}, {self.country}"