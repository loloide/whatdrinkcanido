from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Drink(models.Model):
    name = models.CharField(max_length=30)
    recipe = models.TextField()
    cover_image = models.ImageField(upload_to='drink_pictures/', blank=True, null=True)
    ingredients = models.ManyToManyField(Ingredient, related_name='drinks')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
