from django.db import models

# Create your models here.
class usersignup(models.Model):
    fullname=models.CharField(max_length=20)
    email=models.EmailField()
    mobile=models.BigIntegerField()
    password=models.CharField(max_length=20)