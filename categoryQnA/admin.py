from django.contrib import admin

# Register your models here.
from django.urls import reverse
from django.utils.html import format_html

from .models import CategoryQnA
from django.contrib.auth import get_permission_codename
from django import forms
from django.db import models

import categoryQnAExamples.models as categoryQnAExamplesModel
# # Register your models here.
# def show_examples(modeladmin, request, queryset):
#     # selected_ids = ','.join(str(CategoryQnA.id) for CategoryQnA in queryset)
#     selected_ids=','.join(str(obj.pk) for obj in queryset)
#     url = reverse('categoryQnAExamples:show-examples') + f'?question_ids={selected_ids}'
#     return format_html('<a href="{}" target="_blank">Show Examples</a>', url)

# # show_examples.allowed_permissions = ["publish"]
# show_examples.short_description = 'Show Examples'


class CategoryQnAForm(forms.ModelForm):
    class Meta:
        model = CategoryQnA
        fields = ["question",'answer']
        widgets = {
            'answer': forms.Textarea(attrs={'rows': 2, 'cols': 50}),
            'answer': forms.Textarea(attrs={'rows': 20, 'cols': 500}),
        }

# class CategoryQnAForm(forms.ModelForm):
#     answer = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 50}))

#     class Meta:
#         model = CategoryQnA
#         fields = ['answer']


@admin.register(CategoryQnA)
class CategoryQnA(admin.ModelAdmin):
    # form = CategoryQnAForm
    list_display = ["question","formatted_answer","show_examples_link","reference_links"]
    # actions = [show_examples]
    list_filter = ["category_id__name"]
    search_fields = ('category_id',)

    # formfield_overrides = {
    #     models.TextField: {'widget': forms.Textarea(attrs={'cols': 500})},
    # }



    # def get_form(self, request, obj=None, **kwargs):
    #     kwargs['form'] = CategoryQnAForm
    #     return super().get_form(request, obj, **kwargs)
    def formatted_answer(self, obj):
        return format_html('<textarea style="width:550px; height:200px;"  readonly>{}</textarea>', obj.answer)
    formatted_answer.short_description = "Answer (Textarea)"
    # def formatted_answer(self, obj):
    #     return obj.answer.replace("\n", "<br>")
    # formatted_answer.allow_tags = True
    # formatted_answer.short_description = "Answer (formatted)"

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'answer':
            kwargs['widget'] = admin.widgets.AdminTextareaWidget(attrs={'rows': 20,'cols': 500, 'style': 'width: 100%;'})
        return super().formfield_for_dbfield(db_field, **kwargs)



    def show_examples_link(self, obj):
        if categoryQnAExamplesModel.CategoryQnAExamples.objects.filter(categoryQnA_id=obj.id).exists():
            url = reverse('categoryQnAExamples:show-examples') + f'?question_ids={obj.id}'
            return format_html('<a href="{}" target="_blank">Show Examples</a>', url)
    show_examples_link.short_description = 'Show Examples'
    show_examples_link.allow_tags = True

    # def get_actions(self, request):
    #     actions = super().get_actions(request)
    #     actions['show_examples'] = (show_examples, 'show_examples', 'Show Examples')
    #     return actions

#     def has_publish_permission(self, request):
# #         """Does the user have the publish permission?"""
#         opts = self.opts
#         codename = get_permission_codename("publish", opts)
#         print(codename)
#         print(("%s.%s" % (opts.app_label, codename)))
#         return True
#     # request.user.has_perm("%s.%s" % (opts.app_label, codename))



# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ["question","answer"]
#     actions = [show_examples]
#     list_filter = ["category_id__name"]
#     search_fields = ('category_id',)

    


#     @admin.action(permissions=["publish"])
#     def show_examples(modeladmin, request, queryset):
#         selected_ids=','.join(str(obj.pk) for obj in queryset)
#         url = reverse('admin1:show-examples') + f'?question_ids={selected_ids}'
#         return format_html('<a href="{}" target="_blank">Show Examples</a>', url)

#     def has_publish_permission(self, request):
#         """Does the user have the publish permission?"""
#         opts = self.opts
#         codename = get_permission_codename("publish", opts)
#         return request.user.has_perm("%s.%s" % (opts.app_label, codename))


# admin.site.register(CategoryQnA, ArticleAdmin)