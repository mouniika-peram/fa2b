from django.shortcuts import render

# Create your views here.
from .models import Product
from .serializer import ProductSerializer
from rest_framework import viewsets


class ProductViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

