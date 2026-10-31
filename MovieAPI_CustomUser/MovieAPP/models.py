from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Movie(models.Model):

    title=models.CharField(max_length=50)
    language=models.CharField(max_length=50)
    director=models.CharField(max_length=50)
    year=models.IntegerField()
    runtime=models.IntegerField()
    rating=models.FloatField()
    image=models.ImageField(upload_to="movies",null=True,blank=True)

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20,null=True)
    address = (models.TextField(max_length=100,null=True))
