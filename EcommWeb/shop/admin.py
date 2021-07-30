from django.contrib import admin
from .models import (Customerdetails, Product, Cart, OrderDetails)

# Register your models here.


@admin.register(Customerdetails)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'Name',
                    'Address', 'City', 'Pincode', 'State']


@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'product_price',
                    'category', 'stock_condition', 'product_image']


@admin.register(Cart)
class CartModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product',
                    'quantity']


@admin.register(OrderDetails)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'customer',
                    'product', 'quantity', 'ordered_date', 'status']
