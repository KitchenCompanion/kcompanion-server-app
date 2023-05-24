from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


from .serializers import *
from .models import *
from django.http import HttpResponse 

# Create your views here.
class PersonView(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class RecipeView(ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

class ReviewView(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
