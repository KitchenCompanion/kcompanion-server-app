from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

from .views import UserCreateView

router = DefaultRouter()

router.register('person', views.PersonView)
router.register('review', views.ReviewView)

urlpatterns =  [
    path('recipe/', views.recipe_list),
    path('recipe/<int:id>', views.recipe_detail, name='recipe'),
    path('signup/', UserCreateView.as_view(), name='signup'),
] + router.urls
