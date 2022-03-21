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