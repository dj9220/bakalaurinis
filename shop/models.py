from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(default='category-png-9.png',upload_to='images')
    def __str__(self):
        return self.name
class Supplier(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    adress = models.CharField(max_length=200)
    def __str__(self):
        return self.name
class SubCategories(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(default='category-png-9.png',upload_to='images')
    def __str__(self):
        return self.name
class Matts(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name



class Product(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.FloatField(default=0)
    subCategory = models.ForeignKey(SubCategories,on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE)
    image = models.ImageField(default='category-png-9.png', upload_to='images')
    price = models.FloatField(default=0)
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("shop:all_products")

class ProductInCheck(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.FloatField(default=0)
    def __str__(self):
        return self.product.name
class Check(models.Model):
    products = models.ForeignKey(ProductInCheck,on_delete=models.CASCADE)
    total = models.FloatField(default=0)
    price = models.FloatField(default=0)
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE, default=1)
