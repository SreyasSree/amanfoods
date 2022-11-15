from django.shortcuts import render , redirect
from product.models import Category , Product
from .cart import Cart
from .forms import OrderForm
from .models import Order , OrderItem



# Create your views here.

def cart_list(request):
    cart = Cart(request)
    return render(request , 'cart/cart.html',{'cart':cart})




def cart_add(request,pk):
    cart = Cart(request)
    cart.add(pk)
   

    return redirect('cart:cart_list')


def cart_remove(request,pk):
        cart = Cart(request)
        cart.remove(pk)
        return redirect('cart:cart_list')

def checkout(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save()

            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                )
            cart.clear()
            return redirect('home:success')
            


    form = OrderForm()

    context ={
        'form':form,
        'cart':cart,
    }
    return render(request ,'cart/checkout.html',context)