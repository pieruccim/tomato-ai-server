from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Ingredient, Recipe, Restaurant
from .forms import IngredientForm, RecipeForm, RestaurantForm

from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema

# Ingredient views

@swagger_auto_schema(method='get', responses={200: 'OK'})
@api_view(['GET'])
def ingredient_list(request):
    """
    Get a list of ingredients.
    """
    ingredients = Ingredient.objects.all()
    return render(request, 'ingredient_list.html', {'ingredients': ingredients})

@swagger_auto_schema(methods=['get', 'post'], responses={200: 'OK', 201: 'Created'})
@api_view(['GET', 'POST'])
def ingredient_create(request):
    """
    Create a new ingredient or display creation form.
    """
    if request.method == 'POST':
        form = IngredientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('ingredient-list')
    else:
        form = IngredientForm()
    return render(request, 'ingredient_form.html', {'form': form})

@swagger_auto_schema(methods=['get', 'post'], responses={200: 'OK', 201: 'Created'})
@api_view(['GET', 'POST'])
def ingredient_update(request, pk):
    """
    Update an existing ingredient or display update form.
    """
    ingredient = get_object_or_404(Ingredient, pk=pk)
    if request.method == 'POST':
        form = IngredientForm(request.POST, instance=ingredient)
        if form.is_valid():
            form.save()
            return redirect('ingredient-list')
    else:
        form = IngredientForm(instance=ingredient)
    return render(request, 'ingredient_form.html', {'form': form})

@swagger_auto_schema(method='post', responses={200: 'OK', 204: 'No Content'})
@api_view(['POST'])
def ingredient_delete(request, pk):
    """
    Delete an existing ingredient.
    """
    ingredient = get_object_or_404(Ingredient, pk=pk)
    if request.method == 'POST':
        ingredient.delete()
        return redirect('ingredient-list')

@swagger_auto_schema(methods=['get'], responses={200: 'OK'})
@api_view(['GET'])
def ingredient_detail(request, pk):
    ingredient = get_object_or_404(Ingredient, pk=pk)
    return render(request, 'ingredient_detail.html', {'ingredient': ingredient})

# Recipe views

@swagger_auto_schema(method='get', responses={200: 'OK'})
@api_view(['GET'])
def recipe_list(request):
    """
    Get a list of recipes.
    """
    recipes = Recipe.objects.all()
    return render(request, 'recipe_list.html', {'recipes': recipes})

@swagger_auto_schema(methods=['get', 'post'], responses={200: 'OK', 201: 'Created'})
@api_view(['GET', 'POST'])
def recipe_create(request):
    """
    Create a new recipe or display creation form.
    """
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('recipe-list')
    else:
        form = RecipeForm()
    return render(request, 'recipe_form.html', {'form': form})

@swagger_auto_schema(methods=['get', 'post'], responses={200: 'OK', 201: 'Created'})
@api_view(['GET', 'POST'])
def recipe_update(request, pk):
    """
    Update an existing recipe or display update form.
    """
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe-list')
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipe_form.html', {'form': form})

@swagger_auto_schema(methods=['post'], responses={200: 'OK', 204: 'No Content'})
@api_view(['POST'])
def recipe_delete(request, pk):
    """
    Delete an existing recipe.
    """
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == 'POST':
        recipe.delete()
        return redirect('recipe-list')

@swagger_auto_schema(methods=['get'], responses={200: 'OK'})
@api_view(['GET'])
def recipe_detail(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipe_detail.html', {'recipe': recipe})


# Restaurant views

@swagger_auto_schema(method='get', responses={200: 'OK'})
@api_view(['GET'])
def restaurant_list(request):
    """
    Get a list of restaurants.
    """
    restaurants = Restaurant.objects.all()
    return render(request, 'restaurant_list.html', {'restaurants': restaurants})

@swagger_auto_schema(methods=['get', 'post'], responses={200: 'OK', 201: 'Created'})
@api_view(['GET', 'POST'])
def restaurant_create(request):
    """
    Create a new restaurant or display creation form.
    """
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurant-list')
    else:
        form = RestaurantForm()
    return render(request, 'restaurant_form.html', {'form': form})

@swagger_auto_schema(methods=['get', 'post'], responses={200: 'OK', 201: 'Created'})
@api_view(['GET', 'POST'])
def restaurant_update(request, pk):
    """
    Update an existing restaurant or display update form.
    """
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == 'POST':
        form = RestaurantForm(request.POST, instance=restaurant)
        if form.is_valid():
            form.save()
            return redirect('restaurant-list')
    else:
        form = RestaurantForm(instance=restaurant)
    return render(request, 'restaurant_form.html', {'form': form})

@swagger_auto_schema(method='post', responses={200: 'OK', 204: 'No Content'})
@api_view(['POST'])
def restaurant_delete(request, pk):
    """
    Delete an existing restaurant.
    """
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == 'POST':
        restaurant.delete()
        return redirect('restaurant-list')

@swagger_auto_schema(methods=['get'], responses={200: 'OK'})
@api_view(['GET'])
def restaurant_detail(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    return render(request, 'restaurant_detail.html', {'restaurant': restaurant})