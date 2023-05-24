from django.db import models

# Create your models here.
class Person(models.Model):
    username = models.CharField(max_length = 45)
    password = models.CharField(max_length= 30)

    def __str__(self):
        return self.username


class Recipe(models.Model):
    title = models.CharField(max_length = 45)
    ingredients = models.TextField(max_length = 255)
    steps = models.TextField()
    author = models.ForeignKey(Person, on_delete = models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now = True)
    

    def __str__(self):
        return self.title


class Review(models.Model):
    title = models.CharField(max_length=45)
    description = models.TextField(max_length= 255)
    date_posted = models.DateField()
    reviewer = models.ForeignKey(Person, on_delete = models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete = models.CASCADE)

    def __str__(self):
        return self.title