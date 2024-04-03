from django.contrib import admin

from .models import Category
# Register your models here.
@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ["name"]
    ordering = ["name"]
