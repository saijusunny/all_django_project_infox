from django.db import models

# Create your models here.
class ProductDetails(models.Model):
    product_name=models.CharField(max_length=255)
    description=models.TextField()
    image=models.ImageField(upload_to="image/", null=True)
    product_quantity=models.IntegerField()
    product_price=models.IntegerField()