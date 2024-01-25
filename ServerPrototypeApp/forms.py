from django import forms
from .models import Ingredient, Recipe, Restaurant

class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['_name']
        
        
class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['_title', '_ingredients', '_instructions', '_restaurant']
        
    _ingredients = forms.ModelMultipleChoiceField(
        queryset=Ingredient.objects.all(),
        to_field_name='_name',
        widget=forms.CheckboxSelectMultiple,
    )
    
    _restaurant = forms.ModelChoiceField(
        queryset=Restaurant.objects.all(),
        to_field_name='_name',
        empty_label="Select restaurant"
    )
    

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = ['_name', '_location']
