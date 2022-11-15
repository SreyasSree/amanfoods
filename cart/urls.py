from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('cart_list/',views.cart_list,name='cart_list'),
    path('checkout/',views.checkout,name='checkout'),

    path('cart_add/<int:pk>',views.cart_add,name='cart_add'),
    path('cart_remove/<int:pk>',views.cart_remove,name='cart_remove'),
    
]