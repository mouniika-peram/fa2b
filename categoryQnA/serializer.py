from .models import CategoryQnA
from rest_framework import serializers


class categoryQnASerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryQnA
        fields = ("__all__")
