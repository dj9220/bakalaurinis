from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=12)
    email = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images')
    def __str__(self):
        return self.name
class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    message_content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)