from django.shortcuts import render

# Create your views here.

from django.shortcuts import get_object_or_404

from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404



def Record_Exist_Or_Not(model,id):
    try:
        return get_object_or_404(model,pk=id)
    except Http404:
        return None


def Record_Exist_Or_Not_With_MultiParams(model,parameter_dict):
    try:
        return get_object_or_404(model,**parameter_dict)
    except Http404:
        return None