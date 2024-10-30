from django.contrib import admin
from jet.admin import CompactInline
from .models import Shop, Category, Product, ProductInfo, Parameter, ProductParameter, Order, OrderItem, Contact, DeliveryAddress

# Регистрируем модели в админке
class ShopAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')
    search_fields = ('name', 'url')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category')
    search_fields = ('name',)
    list_filter = ('category',)

class ProductInfoAdmin(admin.ModelAdmin):
    list_display = ('product', 'shop', 'quantity', 'price', 'price_rrc')
    search_fields = ('product__name', 'shop__name')
    list_filter = ('shop', 'product')

class ParameterAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class ProductParameterAdmin(admin.ModelAdmin):
    list_display = ('product_info', 'parameter', 'value')
    search_fields = ('product_info__product__name', 'parameter__name')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'dt', 'status')
    search_fields = ('user__username', 'status')
    list_filter = ('status',)

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'shop', 'quantity')
    search_fields = ('order__id', 'product__name', 'shop__name')
    list_filter = ('order', 'shop')

class ContactAdmin(admin.ModelAdmin):
    list_display = ('type', 'user', 'value')
    search_fields = ('user__username', 'value')
    list_filter = ('type',)

class DeliveryAddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'address_line', 'city', 'postal_code', 'country')

# Регистрируем все модели с их административными настройками
admin.site.register(Shop, ShopAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductInfo, ProductInfoAdmin)
admin.site.register(Parameter, ParameterAdmin)
admin.site.register(ProductParameter, ProductParameterAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(DeliveryAddress, DeliveryAddressAdmin)
