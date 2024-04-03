from django.db import models

# Create your models here.

import categoryQnA.models as CategoryQnAModel



class CategoryQnAExamples(models.Model):
    categoryQnA_id=models.ForeignKey(CategoryQnAModel.CategoryQnA,on_delete=models.CASCADE)
    example=models.TextField(blank=True)
    reference_links=models.TextField(null=True, blank=True)


    def __str__(self):
        return self.categoryQnA_id.question