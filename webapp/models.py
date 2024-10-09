from django.db import models

# Create your models here.
class contactdb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Subject=models.CharField(max_length=100,null=True,blank=True)
    Message=models.CharField(max_length=100,null=True,blank=True)
    Mobile=models.IntegerField(null=True,blank=True)

class signup_db(models.Model):
    Username=models.CharField(max_length=100,null=True,blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Password = models.IntegerField(null=True, blank=True)
    Confirm_Password = models.IntegerField(null=True, blank=True)
    Profileimage=models.ImageField(upload_to="category images",null=True,blank=True)
class cartdb(models.Model):
    Username = models.CharField(max_length=100, null=True, blank=True)
    Productname=models.CharField(max_length=100, null=True, blank=True)
    Quantity=models.IntegerField(null=True, blank=True)
    Totalprice=models.IntegerField(null=True, blank=True)

class checkoutdb(models.Model):
    Username = models.CharField(max_length=100, null=True, blank=True)
    Email=models.EmailField(max_length=100,null=True,blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    Phone= models.IntegerField(null=True, blank=True)
    Total= models.IntegerField(null=True, blank=True)
    saysomething=models.CharField(max_length=100, null=True, blank=True)




