from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model


class Category(models.Model):
    name = models.CharField(max_length=50)
    user_id=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)

    def __str__(self) -> str:
        return  self.name
    