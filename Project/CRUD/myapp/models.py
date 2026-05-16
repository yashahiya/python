from django.db import models

# Create your models here.
class studinfo(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    dob=models.DateField()
    mob=models.BigIntegerField()
    address=models.TextField()
    