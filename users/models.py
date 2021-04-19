from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=11)
    email = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    def __str__(self):
        return self.name
