
from django.db import models

# Create your models here.

class title(models.Model):
    title=models.CharField(max_length=255)
    items=models.ImageField(upload_to="product/items", null=True, blank=True)
    def __str__(self):
        return self.title

class product(models.Model):
    title = models.ForeignKey(title, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to="product/image", null=True, blank=True)