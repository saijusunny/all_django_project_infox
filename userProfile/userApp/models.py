from distutils.command.upload import upload
from hashlib import blake2b
from unicodedata import category
from django.db import models

# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    addrress = models.TextField()
    image = models.ImageField(upload_to="image/", null=True)

    def __str__(self):
        return self.name

#......upload multiple images...
class title(models.Model):
    title = models.CharField(max_length=100)
    itmes = models.ImageField(upload_to='product/items',null=True,blank=True)

    def __str__(self):
        return self.title

class product(models.Model):
    title = models.ForeignKey(title,on_delete=models.CASCADE,null=True,blank=True)
    image = models.ImageField(upload_to='product/image',null=True,blank=True)

#.......Gallery.......
class Category(models.Model):
    category_name = models.CharField(max_length=225)

    def __str__(self):
        return self.category_name

class multimage(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    multimage = models.ImageField(upload_to="multi/image",null=True,blank=True)
    price = models.IntegerField()

class Images(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    image = models.ImageField(upload_to="image/",null=True)
    description = models.CharField(max_length=225)

    def __str__(self):
        return self.description
