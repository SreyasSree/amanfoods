from django.shortcuts import render
from product.models import Category , Product
from cart.models import OrderItem , Order


def order(request):
    orders = Order.objects.all()
    return render(request,'order/order.html',{'orders':orders})

def ordersingle(request,pk):
    orders = Order.objects.get(pk=pk)
    single = OrderItem.objects.filter(order=orders)
    return render(request, 'order/ordersingle.html',{'single':single})