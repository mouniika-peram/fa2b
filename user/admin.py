from django.contrib import admin

# Register your models here.

from .models import CustomUser

# admin.site.register(CustomUser)



@admin.register(CustomUser)
class CustomUser(admin.ModelAdmin):
    search_fields = ('username', 'first_name', 'last_name', 'email')

