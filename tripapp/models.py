# from django.contrib.auth.models import AbstractUser
from django.db import models
from phone_field import PhoneField
from phonenumber_field.modelfields import PhoneNumberField
# class CustomUser(AbstractUser):
#     name = models.CharField(blank=True, max_length=255)

#     def __str__(self):
#         return self.email



# class Clients(models.Model):
#     name = models.CharField(max_length=100)
#     currentLocation = models.TextField()
#     destination = models.TextField()
#     tel = models.IntegerField(default=0)
#     booked = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.name

#     def body_preview(self):
#         return self.body[:50]
class Client(models.Model):
    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    currentLocation = models.CharField(max_length=30)
    Time = models.TimeField()
    destination = models.CharField(max_length=30)
class Entries(models.Model):
    name = models.CharField(max_length=30)
    tel = models.IntegerField(default=0)
    permit = models.TextField()
    age = models.IntegerField(default=0)

