from django.db import models

# Create your models here.
class Entries(models.Model):
    name = models.CharField(max_length=30)
    tel = models.IntegerField(default=0)
    permit = models.TextField()
    age = models.IntegerField(default=0)

