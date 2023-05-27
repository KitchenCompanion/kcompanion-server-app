from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

router = DefaultRouter()

# router.register('User', views.UserView)
router.register('review', views.ReviewView)
# router.register('recipe', views.recipe_list)

urlpatterns =  [
    # path('recipe/', views.recipe_list),
    path('recipe/', views.RecipeCreateView.as_view(), name='recipe'),
    path('recipe/<int:id>', views.recipe_detail, name='recipe'),
    path('signup/', views.UserCreateView.as_view(), name='signup'), 
    path('login/', views.UserLoginApiView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='rest_logout'),
] + router.urls
