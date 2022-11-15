from django.db import models
from product.models import Product , Category

# Create your models here.

class Order(models.Model):
    customer_id = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    Phone = models.CharField(max_length=50)

    def __str__(self):
        return self.customer_id


class OrderItem(models.Model):
    order = models.ForeignKey(Order ,on_delete= models.CASCADE)
    product = models.ForeignKey(Product ,on_delete= models.CASCADE)
