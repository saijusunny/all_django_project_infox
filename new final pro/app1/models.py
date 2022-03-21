

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userlogin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name=models.CharField(max_length=255)
    username=models.CharField(max_length=255)
    password=models.IntegerField()
    repassword=models.IntegerField()
    image=models.ImageField(upload_to="image/", null=True)
    email=models.CharField(max_length=255)


#......upload multiple images...
class title(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    itmes = models.ImageField(upload_to='product/items',null=True,blank=True)
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.title


class curt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    itmes = models.ImageField(upload_to='product/items',null=True,blank=True)
    price = models.IntegerField(null=True)