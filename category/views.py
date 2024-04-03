from django.shortcuts import render
from .models import Ca
# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response

class CartViewset(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def create(self, request, *args, **kwargs):

        quesitons=["What is React.js and what problem does it solve?","Explain the concept of virtual DOM in React.js.",
        "What are components in React? Differentiate between functional and class components.",
        "What are props and state in React? How are they different?",
        "Explain the lifecycle methods of a React component.",
        "What is JSX? Why is it used in React?",
        "What is the significance of keys in React lists?",
        "What are controlled components in React forms?",
        "Explain the concept of higher-order components (HOCs) in React.",
        "How does React Router work? What are its main components?"]