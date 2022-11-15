from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.TextField()
    image = models.ImageField()
    price = models.IntegerField()
    category = models.ForeignKey('Category',on_delete= models.CASCADE)
    quantity = models.CharField(max_length=20)

    def __str__(self):
        return self.title