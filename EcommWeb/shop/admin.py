from django.contrib import admin
from .models import (Customerdetails, Product, Cart,
                     OrderDetails, ProductReview)

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


@admin.register(ProductReview)
class ProductReviewModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product',
                    'review_title', 'review_detail', 'rating']
