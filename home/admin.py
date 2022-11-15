from django.contrib import admin
from product.models import Category , Product
from cart.models import Order , OrderItem



# Register your models here.

admin.site.register(Category)
admin.site.register(Product)


class OrderItemInline(admin.TabularInline):
    model = OrderItem

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]