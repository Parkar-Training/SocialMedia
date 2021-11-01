from django.http import QueryDict
from django.views.decorators.http import require_http_methods
from requests import post,put
from rest_framework.decorators import renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from user.emailOtpSerialization import *
from user.models import users_new
from user.serialization import serializerClass
from user.passwdserialization import *
import hashlib

class SignUp(APIView):

    print("class user list started")

    def get(self, request):
        model = users_new.objects.all()
        print("get start function")

        serializer  = serializerClass(model,many=True)
        return Response(serializer.data)

    def post(self,request):

        serializer = PasswdserializerClass(data=request.data)

        password=request.data['password']
        hash_password = hashlib.md5(password.encode()).hexdigest()
        print(hash_password)
        print(request.data)
        #request.data['password'] = hash_password
        print(type(request.data))

        #requestDataDict = request.data.dict()
        print("req data type dict: ", request.data['password'])
        request.data['password'] = hash_password
        #print(requestDataDict)
        requestDataQueryDict = QueryDict('', mutable=True)
        requestDataQueryDict.update(request.data)
        #requestDataQueryDict.update(requestDataDict)
        print(requestDataQueryDict)
        print(type(requestDataQueryDict))

        serializer = PasswdserializerClass(data=requestDataQueryDict)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)