from django.db import models

# Create your models here.
class Category_db(models.Model):
    Category_Name=models.CharField(max_length=100,blank=True,null=True)
    Description=models.CharField(max_length=100,blank=True,null=True)
    Category_image=models.ImageField(upload_to="category images",null=True,blank=True)



class product_db(models.Model):
    Category=models.CharField(max_length=100,blank=True,null=True)
    Product_name=models.CharField(max_length=100,blank=True,null=True)
    Price=models.IntegerField(null=True,blank=True)
    pro_Description=models.CharField(max_length=100,blank=True,null=True)
    pro_image=models.ImageField(upload_to="category images",null=True,blank=True)
