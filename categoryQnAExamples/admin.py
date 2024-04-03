from django.contrib import admin

# Register your models here.
# categoryQnAExamples

from .models import CategoryQnAExamples
# Register your models here.



@admin.register(CategoryQnAExamples)
class CategoryQnAExamples(admin.ModelAdmin):
    list_display = ["question"]
    list_filter = ["categoryQnA_id__category_id__name"]
    # search_fields = ('category_id',)

    def question(self, object):
        return object.categoryQnA_id.question

    def answer(self, object):
        return object.categoryQnA_id.answer