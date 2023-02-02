from django.db import models
 
# Create your models here.
class food(models.Model):
    name= models.CharField(max_length=100)
    desc= models.TextField()
    image= models.ImageField(upload_to='food_images')
    price= models.IntegerField()
    type = models.TextField()
    d_price = models.IntegerField(default=0)
    active = models.BooleanField(default=True)
class order(models.Model):
    username = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    food = models.CharField(max_length=100)
    quantity = models.IntegerField(null= True)
    time = models.DateTimeField(auto_now_add=True)
    total_price = models.IntegerField()