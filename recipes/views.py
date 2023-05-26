from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from rest_framework.decorators import APIView

from rest_framework.authentication import TokenAuthentication
from django.contrib.auth import get_user_model
from rest_framework import generics
from .serializers import UserCreateSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import AuthTokenSerializer
from rest_framework.settings import api_settings

from .serializers import *
from .models import *
from django.http import HttpResponse 

# Create your views here.
User = get_user_model()

# Sign-up/Create user view
class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer

# Login View

class UserLoginApiView(ObtainAuthToken):
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES #Allow for rendering in deifferent formats; JSON< XML...
    

# Logout View
class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class ReviewView(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer



class recipe_list(ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
# @api_view(['GET', 'POST'])
# def recipe_list(request):

#     if request.method == 'GET':
#         recipe = Recipe.objects.all()
#         serializer = RecipeSerializer(recipe, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = RecipeSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def recipe_detail(request, id):

    try:
        recipe = Recipe.objects.get(pk = id)
    except Recipe.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RecipeSerializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    elif request.method == 'DELETE':
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)