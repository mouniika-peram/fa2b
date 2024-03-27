from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
import product.models as prd_models

class CommonInfo(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class Cart(CommonInfo):
    user_id=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    prd_id=models.ForeignKey(prd_models.Product,on_delete=models.CASCADE)
    prd_title=models.CharField(max_length=100)
    prd_img=models.ImageField()
    prd_price=models.FloatField(default=0)
    qty=models.FloatField(default=0)
    net_amt=models.FloatField(default=0)





