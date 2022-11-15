from django.shortcuts import render
from product.models import Category , Product

# Create your views here.

def index(request):
    cat = Category.objects.all()
    pro = Product.objects.all()[:4]


    context ={
        'cat':cat,
        'pro':pro,
    }
    return render(request , 'home/index.html',context)







def success(request):
    return render(request , 'success.html')