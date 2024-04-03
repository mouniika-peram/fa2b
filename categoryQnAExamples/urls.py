from django.urls import path
from .views import show_examples

app_name = 'categoryQnAExamples'

urlpatterns = [
    # Other URL patterns
    path('admin1/show-examples/', show_examples, name='show-examples'),
]
