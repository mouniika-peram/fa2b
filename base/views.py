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
    









# -----------------------------
    
# Token  Authrntication
    
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from user.serializer import CustomUserSerializer

class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        # import pdb;pdb.set_trace();
        # serializer = self.serializer_class(data=request.data,context={'request': request})
        serializer =CustomUserSerializer(data=request.data,context={'request': request})
        serializer.is_valid(raise_exception=True)
        # user = serializer.data
        user=serializer.save()
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })
# ------------------------------------------------------------