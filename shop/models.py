from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    subcategories = models.ManyToManyField("self", blank=True)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    adress = models.CharField(max_length=200)


class Product(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.FloatField()
    description = models.CharField(max_length=500, blank=True, default="")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    image = models.ImageField(default='category-png-9.png', upload_to='images')
