from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view

from django.contrib.auth import get_user_model
from rest_framework import generics
from .serializers import UserCreateSerializer

from .serializers import *
from .models import *
from django.http import HttpResponse 

# Create your views here.
User = get_user_model()

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer

    
class PersonView(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class ReviewView(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


@api_view(['GET', 'POST'])
def recipe_list(request):

    if request.method == 'GET':
        recipe = Recipe.objects.all()
        serializer = RecipeSerializer(recipe, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = RecipeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

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