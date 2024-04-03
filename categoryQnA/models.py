from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
import category.models as CategoryModel



class CategoryQnA(models.Model):
    category_id= models.ForeignKey(CategoryModel.Category,on_delete=models.CASCADE)
    question=models.TextField()
    answer=models.TextField()
    user_id=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    reference_links=models.TextField(null=True, blank=True)
    
    def __str__(self) -> str:
        return  self.question
    




