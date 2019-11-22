# from django.contrib.auth.models import AbstractUser
from django.db import models
from phone_field import PhoneField
# Create your models here.
class Entries(models.Model):
    name = models.CharField(max_length=30)
    tel = models.IntegerField(help_text='Contact phone number')
    permit = models.TextField()
    email = models.EmailField()
    user_id = models.CharField(max_length=30)
    platenbr = models.CharField(max_length=30)
    
class Client(models.Model):
    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    currentLocation = models.CharField(max_length=30)
    Time = models.TimeField()
    destination = models.CharField(max_length=30)
