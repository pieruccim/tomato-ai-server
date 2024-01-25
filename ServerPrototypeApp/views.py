from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Ingredient, Recipe, Restaurant
from .forms import IngredientForm, RecipeForm, RestaurantForm

# Ingredient views

class IngredientListView(ListView):
    model = Ingredient
    template_name = 'ingredient_list.html'

class IngredientCreateView(CreateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'ingredient_form.html'
    
    def get_success_url(self):
        return reverse_lazy('ingredient-list')

class IngredientUpdateView(UpdateView):
    model = Ingredient
    form_class = IngredientForm
    template_name = 'ingredient_form.html'
    
    def get_success_url(self):
        return reverse_lazy('ingredient-list')

class IngredientDeleteView(DeleteView):
    model = Ingredient
    template_name = 'ingredient_confirm_delete.html'
    success_url = reverse_lazy('ingredient-list')
    
# Recipe views

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe_list.html'

class RecipeCreateView(CreateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe_form.html'

    def get_success_url(self):
        return reverse_lazy('recipe-list')

class RecipeUpdateView(UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'recipe_form.html'

    def get_success_url(self):
        return reverse_lazy('recipe-list')

class RecipeDeleteView(DeleteView):
    model = Recipe
    template_name = 'recipe_confirm_delete.html'
    success_url = reverse_lazy('recipe-list')

# Restaurant views

class RestaurantListView(ListView):
    model = Restaurant
    template_name = 'restaurant_list.html'

class RestaurantCreateView(CreateView):
    model = Restaurant
    form_class = RestaurantForm
    template_name = 'restaurant_form.html'

    def get_success_url(self):
        return reverse_lazy('restaurant-list')

class RestaurantUpdateView(UpdateView):
    model = Restaurant
    form_class = RestaurantForm
    template_name = 'restaurant_form.html'

    def get_success_url(self):
        return reverse_lazy('restaurant-list')

class RestaurantDeleteView(DeleteView):
    model = Restaurant
    template_name = 'restaurant_confirm_delete.html'
    success_url = reverse_lazy('restaurant-list')
