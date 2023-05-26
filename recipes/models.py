from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.models import UserManager

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=30, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def _str_(self):
        return self.email

# class User(models.Model):
#     username = models.CharField(max_length = 45)
#     password = models.CharField(max_length= 30)

#     def __str__(self):
#         return self.username


class Recipe(models.Model):
    title = models.CharField(max_length = 45)
    ingredients = models.TextField(max_length = 255)
    steps = models.TextField()
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now = True)
    rating = models.DecimalField(max_digits=5, decimal_places=1)
    

    def __str__(self):
        return self.title


class Review(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField(max_length= 255)
    date_posted = models.DateField()
    reviewer = models.ForeignKey(User, on_delete = models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)

    def __str__(self):
        return self.title