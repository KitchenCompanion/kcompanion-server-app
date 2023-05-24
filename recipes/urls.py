from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('person', views.PersonView)
router.register('recipe', views.RecipeView)
router.register('review', views.ReviewView)

urlpatterns =  router.urls