from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class adduser_model(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    gender=models.CharField(max_length=255)
    image=models.ImageField(upload_to='image/')

class catogery_model(models.Model):
    name=models.CharField(max_length=255)

class add_product_model(models.Model):
    catogery=models.ForeignKey(catogery_model,on_delete=models.CASCADE)
    image=models.ImageField(upload_to='image/',default="static/images/no-photo-icon-loading-images-.jpg")
    name=models.CharField(max_length=255)
    price=models.IntegerField()
    quantity=models.IntegerField()
    availability=models.CharField(max_length=255,default="instock")

class add_cart(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    product=models.ForeignKey(add_product_model,on_delete=models.CASCADE)
