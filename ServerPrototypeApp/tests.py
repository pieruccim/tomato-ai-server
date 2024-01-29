from django.test import TestCase
from django.test import RequestFactory
from django.urls import reverse
from .models import Recipe, Restaurant, Ingredient
from .views import (
    ingredient_list_in_recipe,
    ingredient_list_used_by_restaurant,
    ingredient_create,
    ingredient_update,
    ingredient_delete,
    ingredient_detail
)
from django.http import HttpResponse

class IngredientListViewInRecipeTestCase(TestCase):
    def setUp(self):
        self.restaurant1 = Restaurant.objects.create(_name='Restaurant 1')
        self.ingredient1 = Ingredient.objects.create(_name='Ingredient 1')
        self.ingredient2 = Ingredient.objects.create(_name='Ingredient 2')
        self.recipe = Recipe.objects.create(_recipe_id=1, _restaurant=self.restaurant1)
        self.recipe._ingredients.add(self.ingredient1, self.ingredient2)
        self.factory = RequestFactory()

    def test_ingredient_list_in_recipe_view(self):
        request = self.factory.get(reverse('ingredient-list-in-recipe', kwargs={'recipe_id': self.recipe._recipe_id}))
        response = ingredient_list_in_recipe(request, recipe_id=self.recipe._recipe_id)
        self.assertIsInstance(response, HttpResponse)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.ingredient1._name)
        self.assertContains(response, self.ingredient2._name)
