from django.db import models

# Create your models here.

class CommonInfo(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True
        

class Product(CommonInfo):
    name=models.CharField(max_length=100)
    price=models.FloatField(default=0)
    image=models.ImageField(upload_to ='uploads/')
    description=models.TextField(blank=True)

