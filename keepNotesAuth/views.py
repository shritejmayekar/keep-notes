from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import viewsets, routers, serializers
# from TodoAuth.serializers import UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, DjangoModelPermissions
from rest_framework.status import (
    HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_401_UNAUTHORIZED)
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from keepNotesAuth.models import User
# Create your views here.


@api_view(['POST'])
@permission_classes((AllowAny,))
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    if email is None or password is None:
        return Response({'error': 'Please Provide email and password'}, status=HTTP_400_BAD_REQUEST)

    user = authenticate(username=email, password=password)

    if not user:
        return Response({'error': 'Invalid Creditials'}, status=HTTP_401_UNAUTHORIZED)

    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key}, status=HTTP_200_OK)

@api_view(['POST'])
@permission_classes((AllowAny,))
def register(request):
    email = request.data.get('email')
    password = request.data.get('password')
    username = request.data.get('username')

    if email is None or password is None or username is None:
        return Response({'error':'Please provide email,username and password'},status=HTTP_400_BAD_REQUEST)
        
    if len(User.objects.filter(email=email)) > 0:
        return Response({'error':'Email is Already registered'},status=HTTP_400_BAD_REQUEST)
    registered = User.objects.create_user(email=email,password=password,username=username)

    return Response({'success': 'Registered success {}'.format(registered)},status=HTTP_201_CREATED)
