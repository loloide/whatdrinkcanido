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
        "image": drink.image.url if drink.image else None,
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
            "image": drink.image.url if drink.image else None,
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

    drinks = Drink.objects.filter(ingredients__in=ingredients).distinct().order_by('name')

    drinks_data = []
    for drink in drinks:
        drink_ingredient_names = [ingredient.name for ingredient in drink.ingredients.all()]

        if all(ingredient in ingredient_names for ingredient in drink_ingredient_names):
            drink_data = {
                "name": drink.name,
                "desc": drink.recipe,
                "image": drink.image.url if drink.image else None,
                "id": drink.pk,
                "ingredients": drink_ingredient_names,
                "created_at": drink.created_at.isoformat(),
                "updated_at": drink.updated_at.isoformat(),
            }
            drinks_data.append(drink_data)

    return JsonResponse(drinks_data, safe=False)

def search_with_ingredients_allow_missing(request):
    ingredient_list_str = request.GET.get('ingredientlist', '')
    if not ingredient_list_str:
        return JsonResponse({"error": "No ingredients provided"}, status=400)
    ingredient_names = ingredient_list_str.split(',')
    ingredients = Ingredient.objects.filter(name__in=ingredient_names)
    
    if len(ingredients) != len(ingredient_names):
        return JsonResponse({"error": "Some ingredients not found"}, status=404)

    drinks = Drink.objects.filter(ingredients__in=ingredients).distinct()

    drinks_data = []
    for drink in drinks:
        drink_data = {
            "name": drink.name,
            "desc": drink.recipe,
            "image": drink.image.url if drink.image else None,
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
