from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('product/',views.product,name='product'),
    path('product/<int:id>',views.product,name='products'),
    path('productsingle/<int:id>',views.productsingle,name='productsingle'),
    
]