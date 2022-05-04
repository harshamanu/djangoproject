from django.db import models

# Create your models here.
class Signup(models.Model):
    Name=models.CharField(max_length=20)
    Age=models.IntegerField()
    Place=models.CharField(max_length=20)
    Photo=models.ImageField(upload_to='media/',blank=True,null=True)
    Email=models.EmailField()
    Password=models.CharField(max_length=8)
    
class Gallery(models.Model):
    Carname=models.CharField(max_length=20)
    Carmodel=models.CharField(max_length=20)
    Carprize=models.IntegerField()
    Carphoto=models.ImageField(upload_to='media/',blank=True,null=True)    