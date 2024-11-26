from django.contrib import admin
from .models import Ingredient, Drink

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Display the name of the ingredient
    search_fields = ('name',)  # Add a search box for ingredients

@admin.register(Drink)
class DrinkAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')  # Display these fields in the list view
    search_fields = ('name',)  # Add a search box for drinks
    list_filter = ('created_at',)  # Add a filter by creation date
    autocomplete_fields = ('ingredients',)  # Allow easy selection of ingredients