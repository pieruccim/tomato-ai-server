from django.urls import path
from .views import (
    ingredient_list, ingredient_create, ingredient_update, ingredient_delete, ingredient_detail,
    recipe_list, recipe_create, recipe_update, recipe_delete, recipe_detail,
    restaurant_list, restaurant_create, restaurant_update, restaurant_delete, restaurant_detail
)

urlpatterns = [
    
    # Ingredient URLs
    path('ingredients/', ingredient_list, name='ingredient-list'),
    path('ingredients/create/', ingredient_create, name='ingredient-create'),
    path('ingredients/<int:pk>/update/', ingredient_update, name='ingredient-update'),
    path('ingredients/<int:pk>/delete/', ingredient_delete, name='ingredient-delete'),
    path('ingredients/<int:pk>/', ingredient_detail, name='ingredient-detail'),

    # Recipe URLs
    path('recipes/', recipe_list, name='recipe-list'),
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
    
]
