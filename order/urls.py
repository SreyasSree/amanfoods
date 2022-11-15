from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('ordersingle/<int:pk>',views.ordersingle,name='ordersingle'),
    path('order/',views.order,name='order'),

]