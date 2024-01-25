from django.urls import path
from .views import (
    IngredientListView, IngredientCreateView, IngredientUpdateView, IngredientDeleteView,
    RecipeListView, RecipeCreateView, RecipeUpdateView, RecipeDeleteView,
    RestaurantListView, RestaurantCreateView, RestaurantUpdateView, RestaurantDeleteView
)

urlpatterns = [
    
    # Ingredient endpoints
    path('ingredients/', IngredientListView.as_view(), name='ingredient-list'),
    path('ingredients/create/', IngredientCreateView.as_view(), name='ingredient-create'),
    path('ingredients/<int:pk>/update/', IngredientUpdateView.as_view(), name='ingredient-update'),
    path('ingredients/<int:pk>/delete/', IngredientDeleteView.as_view(), name='ingredient-delete'),

    # Recipe endpoints
    path('recipes/', RecipeListView.as_view(), name='recipe-list'),
    path('recipes/create/', RecipeCreateView.as_view(), name='recipe-create'),
    path('recipes/<int:pk>/update/', RecipeUpdateView.as_view(), name='recipe-update'),
    path('recipes/<int:pk>/delete/', RecipeDeleteView.as_view(), name='recipe-delete'),

    # Restaurant endpoints
    path('restaurants/', RestaurantListView.as_view(), name='restaurant-list'),
    path('restaurants/create/', RestaurantCreateView.as_view(), name='restaurant-create'),
    path('restaurants/<int:pk>/update/', RestaurantUpdateView.as_view(), name='restaurant-update'),
    path('restaurants/<int:pk>/delete/', RestaurantDeleteView.as_view(), name='restaurant-delete'),
]
