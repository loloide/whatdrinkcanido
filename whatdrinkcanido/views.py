from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.db.models import Q, Count
from itertools import combinations
from .models import Drink, Ingredient

def drink_detail(request, pk):
    drink = get_object_or_404(Drink, pk=pk)

    drink_data = {
        "name": drink.name,
        "desc": drink.recipe,
        "cover_image": drink.cover_image.url if drink.cover_image else None,
        "id": drink.pk,
        "ingredients": [ingredient.name for ingredient in drink.ingredients.all()],
        "created_at": drink.created_at.isoformat(),
        "updated_at": drink.updated_at.isoformat(),
    }

    return JsonResponse(drink_data)

def search_by_name(request):
    name = request.GET.get('query', '')
    if not name:
        return JsonResponse({"error": "No name provided"}, status=400)

    drinks = Drink.objects.filter(name__contains=name)

    drinks_data = []
    for drink in drinks:
        drink_data = {
            "name": drink.name,
            "desc": drink.recipe,
            "cover_image": drink.cover_image.url if drink.cover_image else None,
            "id": drink.pk,
            "ingredients": [ingredient.name for ingredient in drink.ingredients.all()],
            "created_at": drink.created_at.isoformat(),
            "updated_at": drink.updated_at.isoformat(),
        }
        drinks_data.append(drink_data)
    
    return JsonResponse(drinks_data, safe=False)

def search_with_ingredients(request):
    ingredient_list_str = request.GET.get('ingredientlist', '')
    if not ingredient_list_str:
        return JsonResponse({"error": "No ingredients provided"}, status=400)

    ingredient_names = ingredient_list_str.split(',')
    ingredients = Ingredient.objects.filter(name__in=ingredient_names)

    if len(ingredients) != len(ingredient_names):
        return JsonResponse({"error": "Some ingredients not found"}, status=404)

    ingredient_combinations = []
    for r in range(1, len(ingredient_names) + 1):
        ingredient_combinations.extend(combinations(ingredient_names, r))

    drinks_data = []
    for combo in ingredient_combinations:
        combo_ingredients = Ingredient.objects.filter(name__in=combo)
        drinks = Drink.objects.filter(ingredients__in=combo_ingredients).distinct()
        for drink in drinks:
            drink_ingredients = set(drink.ingredients.values_list('name', flat=True))
            if drink_ingredients == set(combo):  # Drink must have exactly these ingredients
                drink_data = {
                    "name": drink.name,
                    "desc": drink.recipe,
                    "cover_image": drink.cover_image.url if drink.cover_image else None,
                    "id": drink.pk,
                    "ingredients": [ingredient.name for ingredient in drink.ingredients.all()],
                    "created_at": drink.created_at.isoformat(),
                    "updated_at": drink.updated_at.isoformat(),
                }
                drinks_data.append(drink_data)

    return JsonResponse(drinks_data, safe=False)

def search_with_ingredients_allow_missing(request):
    # Get the `ingredientlist` parameter from the request
    ingredient_list_str = request.GET.get('ingredientlist', '')
    if not ingredient_list_str:
        return JsonResponse({"error": "No ingredients provided"}, status=400)

    # Split the ingredient list into individual ingredients
    ingredient_names = ingredient_list_str.split(',')

    # Query the database for the ingredients
    ingredients = Ingredient.objects.filter(name__in=ingredient_names)

    # If some ingredients don't exist, return an error
    if len(ingredients) != len(ingredient_names):
        return JsonResponse({"error": "Some ingredients not found"}, status=404)

    # Find drinks that have all these ingredients
    drinks = Drink.objects.filter(ingredients__in=ingredients).distinct()

    # Serialize the data into a list of drinks with ingredient names
    drinks_data = []
    for drink in drinks:
        drink_data = {
            "name": drink.name,
            "desc": drink.recipe,
            "cover_image": drink.cover_image.url if drink.cover_image else None,
            "id": drink.pk,
            "ingredients": [ingredient.name for ingredient in drink.ingredients.all()],
            "created_at": drink.created_at.isoformat(),
            "updated_at": drink.updated_at.isoformat(),
        }
        drinks_data.append(drink_data)

    return JsonResponse(drinks_data, safe=False)

def get_ingredients(request):
    ingredients = Ingredient.objects.all().order_by('name')

    ingredients_data = []
    for ingredient in ingredients:
        ingredient_data = {
            "name": ingredient.name
        }

        ingredients_data.append(ingredient_data)
    return JsonResponse(ingredients_data, safe=False)
