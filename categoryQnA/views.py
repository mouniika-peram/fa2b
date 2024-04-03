from django.shortcuts import render
from .models import CategoryQnA
# Create your views here.
from rest_framework import viewsets
from rest_framework.response import Response

from .serializer import categoryQnASerializer
from rest_framework.decorators import action



class CategoryQnAViewset(viewsets.ModelViewSet):
    queryset = CategoryQnA.objects.all()
    serializer_class = categoryQnASerializer

    def create(self, request, *args, **kwargs):
        pass



    @action(detail=False,methods=["GET"])
    def categoryqnacreate(self, request, *args, **kwargs):
        # import pdb;pdb.set_trace();
        questions=[
            "What are the differences between let, const, and var in JavaScript?",
            "Explain the concept of hoisting in JavaScript.",
            "What is the event loop in JavaScript, and how does it work?",
            "Describe how prototypal inheritance works in JavaScript.",
            "What are modules in JavaScript, and how do they differ from scripts?",
            "What are template literals, and how do you use them in JavaScript?",
            "How does destructuring assignment work in JavaScript, and when would you use it?",
            "Explain the concept of asynchronous programming in JavaScript.",
            "What are promises in JavaScript, and how do they differ from callbacks?",
            "What are some new features introduced in ES6 (ECMAScript 2015), and how do they improve JavaScript?"
            ]
        
        for que in questions:
            CategoryQnA.objects.create(category_id_id=2,question=que,answer="c",user_id_id=1)

        return Response({"message":"success"})
    
# http://127.0.0.1:8000/api/v1/categoryqna/categoryqnacreate/

