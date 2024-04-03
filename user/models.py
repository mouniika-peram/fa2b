from django.db import models

# Create your models here.

from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    temp_id = models.TextField(blank=True)
    verify_email = models.BooleanField(default=False)

    search_fields = ["email"]
