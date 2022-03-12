from ntpath import join
from django.db import models

from email.policy import default
from django.db import models

# Create your models here.
class userlogin(models.Model):
    name=models.CharField(max_length=255)
    username=models.CharField(max_length=255)
    password=models.IntegerField()
    repassword=models.IntegerField()
    image=models.ImageField(upload_to="image/", null=True)
    email=models.CharField(max_length=255)


#......upload multiple images...
class title(models.Model):
    title = models.CharField(max_length=100)
    amount = models.IntegerField( null=True)
    itmes = models.ImageField(upload_to='product/items',null=True,blank=True)
    

    def __str__(self):
        return self.title

class product(models.Model):
    title = models.ForeignKey(title,on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField(upload_to='product/image',null=True,blank=True)