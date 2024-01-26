from django.urls import path
from .views import (
    ingredient_list, ingredient_create, ingredient_update, ingredient_delete, ingredient_detail, ingredient_list_in_recipe, ingredient_list_used_by_restaurant,
    recipe_list, recipe_list_by_restaurant, recipe_list_by_ingredient, recipe_create, recipe_update, recipe_delete, recipe_detail,
    restaurant_list, restaurant_create, restaurant_update, restaurant_delete, restaurant_detail
)

urlpatterns = [
    
    # Ingredient URLs
    path('ingredients/', ingredient_list, name='ingredient-list'),
    path('ingredients/in-recipe/<int:recipe_id>/', ingredient_list_in_recipe, name='ingredient-list-in-recipe'),
    path('ingredients/used-by-restaurant/<int:restaurant_id>/', ingredient_list_used_by_restaurant, name='ingredient-list-used-by-restaurant'),
    path('ingredients/create/', ingredient_create, name='ingredient-create'),
    path('ingredients/<int:pk>/update/', ingredient_update, name='ingredient-update'),
    path('ingredients/<int:pk>/delete/', ingredient_delete, name='ingredient-delete'),
    path('ingredients/<int:pk>/', ingredient_detail, name='ingredient-detail'),

    # Recipe URLs
    path('recipes/', recipe_list, name='recipe-list'),
    path('recipes/by-restaurant/<int:restaurant_id>/', recipe_list_by_restaurant, name='recipe-list-by-restaurant'),
    path('recipes/by-ingredient/<int:ingredient_id>/', recipe_list_by_ingredient, name='recipe-list-by-ingredient'),
    path('recipes/create/', recipe_create, name='recipe-create'),
    path('recipes/<int:pk>/update/', recipe_update, name='recipe-update'),
    path('recipes/<int:pk>/delete/', recipe_delete, name='recipe-delete'),
    path('recipes/<int:pk>/', recipe_detail, name='recipe-detail'),

    # Restaurant URLs
    path('restaurants/', restaurant_list, name='restaurant-list'),
    path('restaurants/create/', restaurant_create, name='restaurant-create'),
    path('restaurants/<int:pk>/update/', restaurant_update, name='restaurant-update'),
    path('restaurants/<int:pk>/delete/', restaurant_delete, name='restaurant-delete'),
    path('restaurants/<int:pk>/', restaurant_detail, name='restaurant-detail'),
    path('restaurants/filter/', restaurant_list, name='restaurant-list-filtered'),
    
]
