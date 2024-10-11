from django.db import models
from django.conf import settings


# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)



    def __str__(self):
        return self.product_name
    




class user(models.Model):
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.username




