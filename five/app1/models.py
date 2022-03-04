from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class students_admin(models.Model): #students is a table name
    std_id=models.IntegerField()
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    course=models.CharField(max_length=255)
    email=models.EmailField()