from django.contrib import admin
from .models import Product, Order, CartItem, LineItem, Category

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display =['id', 'name', 'category', 'price']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'date', 'paid']


class OrderItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'price', 'quantity', 'product']


class LineItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'price', 'quantity', 'date_added', 'order']


admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(LineItem, LineItemAdmin)
admin.site.register(Category)