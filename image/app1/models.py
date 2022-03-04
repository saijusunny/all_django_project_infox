from django.db import models

# Create your models here.
class images(models.Model): #employees is the table name
    product_name=models.CharField(max_length=255)
    product_price=models.IntegerField()
    image=models.ImageField(upload_to="image/", null=True)
    