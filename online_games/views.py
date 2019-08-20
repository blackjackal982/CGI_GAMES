from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view,APIView,authentication_classes,permission_classes
from rest_framework import status
from .serializers import *

from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication,SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

@api_view(['GET','POST','DELETE','PUT'])
def get_games(request,*args,**kwargs):
    if request.method =='GET':
        if not kwargs:
            try:
                games = Games.objects.all()
                serialized_list = GameSerializer(games, many=True)
                return Response(serialized_list.data)
            except Exception:
                return Response(serialized_list.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            try:
                games = Games.objects.get(id=kwargs.get('pk'))
                serialized_list = GameSerializer(games)
                return Response(serialized_list.data)
            except Exception:
                return Response(serialized_list.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'POST':
        serializer = GameSerializer(data=request.data,context={
            'request':request
        })
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        try:
            game = Games.objects.get(id=kwargs.get('pk'))
        except Games.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    elif request.method == 'PUT':
        game = Games.objects.get(id=kwargs.get('pk'))
        serializer = GameSerializer(game, data=request.data,context={
            'request':request,
        })
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

