from django.shortcuts import render , get_object_or_404
from .models import Category ,Product



# Create your views here.

def product(request,id=None):
    
    if id:
        cate = get_object_or_404(Category,id=id)
        pro = Product.objects.filter(Cate=Category)

        return render(request , 'product/products.html',{'pro':pro,'cate':cate})


    cat = Category.objects.all()
    pro = Product.objects.all()

    context ={
        'cat':cat,
        'pro':pro,
    }
    return render(request , 'product/products.html',context)



def productsingle(request,id):
    # cat = Category.objects.all()
    pro = Product.objects.get(id=id)


    context ={
        # 'cat':cat,
        'pro':pro,
    }
    return render(request , 'product/productsingle.html',context)

