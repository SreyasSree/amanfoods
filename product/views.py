from django.shortcuts import render , get_object_or_404
from .models import Category ,Product



# Create your views here.

def product(request,id=None):
    
    if id:
        cate = get_object_or_404(Category,id=id)
        pro = Product.objects.filter(category=cate)
        cat = Category.objects.all()

        context ={
        'cat':cat,
        'pro':pro,
        'cate':cate,
        }

        return render(request , 'product/products.html',context)

    else:
        pro =Product.objects.all()
        cat =Category.objects.all()

        context ={
        'cat':cat,
        'pro':pro,
        }
        
        return render(request,'product/products.html',context)


    cat = Category.objects.all()
    pro = Product.objects.all()

    context ={
        'cat':cat,
        'pro':pro,
    }
    return render(request , 'product/products.html',context)



def productsingle(request,id):
    cat = Category.objects.all()
    pro = Product.objects.get(id=id)


    context ={
        'cat':cat,
        'pro':pro,
    }
    return render(request , 'product/productsingle.html',context)

