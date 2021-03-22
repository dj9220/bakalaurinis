from django.db import models

# Create your models here.
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(default='category-png-9.png',upload_to='images')
    def __str__(self):
        return self.name
    def getName(self):
        return self.name

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Category.objects.all())
        return super().get(request, *args, **kwargs)
class Supplier(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    adress = models.CharField(max_length=200)
class SubCategories(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category,default=1,on_delete=models.CASCADE,related_name='categories')
    image = models.ImageField(default='category-png-9.png',upload_to='images')
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.FloatField()
    description = models.CharField(max_length=500)
    subCategory = models.ForeignKey(SubCategories,on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier,on_delete=models.CASCADE,default=1)
    image = models.ImageField(default='category-png-9.png', upload_to='images')
