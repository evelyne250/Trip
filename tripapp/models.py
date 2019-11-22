from django.db import models
from phone_field import PhoneField
# Create your models here.
class Entries(models.Model):
    name = models.CharField(max_length=30)
    tel = models.IntegerField(help_text='Contact phone number')
    permit = models.TextField()
    email = models.IntegerField(default=0)
    user_id = models.CharField(max_length=30)
    platenbr = models.CharField(max_length=30)
    
    
