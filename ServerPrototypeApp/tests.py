from django.test import TestCase
from django.test import RequestFactory
from django.urls import reverse
from .models import Recipe, Restaurant, Ingredient
from .views import (
    ingredient_list,
    ingredient_list_in_recipe,
    ingredient_list_used_by_restaurant,
    ingredient_create,
    ingredient_update,
    ingredient_delete,
    ingredient_detail
)
from django.http import HttpResponse

class IngredientListViewTestCase(TestCase):
    def setUp(self):
        # Create sample data
        self.restaurant1 = Restaurant.objects.create(_name='Restaurant 1')
        self.restaurant2 = Restaurant.objects.create(_name='Restaurant 2')
        self.ingredient1 = Ingredient.objects.create(_name='Ingredient 1')
        self.ingredient2 = Ingredient.objects.create(_name='Ingredient 2')
        self.recipe1 = Recipe.objects.create(_recipe_id=1, _restaurant=self.restaurant1)
        self.recipe2 = Recipe.objects.create(_recipe_id=2, _restaurant=self.restaurant2)
        self.recipe1._ingredients.add(self.ingredient1)
        self.recipe2._ingredients.add(self.ingredient2)
        self.factory = RequestFactory()

    def test_ingredient_list_in_recipe_view(self):
        # Test the ingredient list in recipe view
        request = self.factory.get(reverse('ingredient-list-in-recipe', kwargs={'recipe_id': self.recipe1._recipe_id}))
        response = ingredient_list_in_recipe(request, recipe_id=self.recipe1._recipe_id)
        self.assertIsInstance(response, HttpResponse)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.ingredient1._name)
        self.assertNotContains(response, self.ingredient2._name)

    def test_ingredient_list_used_by_restaurant_view(self):
        # Test the ingredient list used by restaurant view
        request = self.factory.get(reverse('ingredient-list-used-by-restaurant', kwargs={'restaurant_id': self.restaurant1._restaurant_id}))
        response = ingredient_list_used_by_restaurant(request, restaurant_id=self.restaurant1._restaurant_id)
        self.assertIsInstance(response, HttpResponse)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.ingredient1._name)
        self.assertNotContains(response, self.ingredient2._name)
        
    def test_ingredient_list_view(self):
        request = self.factory.get(reverse('ingredient-list'))
        response = ingredient_list(request)
        self.assertIsInstance(response, HttpResponse)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.ingredient1._name)
        self.assertContains(response, self.ingredient2._name)

    def test_ingredient_create_view(self):
        # Test the ingredient create view (GET request)
        request = self.factory.get(reverse('ingredient-create'))
        response = ingredient_create(request)
        self.assertIsInstance(response, HttpResponse)
        self.assertEqual(response.status_code, 200)

        # Test the ingredient create view (POST request)
        request = self.factory.post(reverse('ingredient-create'), {'name': 'New Ingredient'})
        response = ingredient_create(request)
        self.assertEqual(response.status_code, 200)

    def test_ingredient_update_view(self):

        # Test the ingredient update view (GET request)
        request = self.factory.get(reverse('ingredient-update', kwargs={'pk': self.ingredient1.pk}))
        response = ingredient_update(request, pk=self.ingredient1.pk)
        self.assertIsInstance(response, HttpResponse)
        self.assertEqual(response.status_code, 200)

        # Test the ingredient update view (POST request)
        request = self.factory.post(reverse('ingredient-update', kwargs={'pk': self.ingredient1.pk}), {'name': 'Updated Ingredient'})
        response = ingredient_update(request, pk=self.ingredient1.pk)
        self.assertEqual(response.status_code, 200)

    def test_ingredient_delete_view(self):

        # Test the ingredient delete view
        request = self.factory.post(reverse('ingredient-delete', kwargs={'pk': self.ingredient1.pk}))
        response = ingredient_delete(request, pk=self.ingredient1.pk)
        self.assertEqual(response.status_code, 302)

    def test_ingredient_detail_view(self):

        # Test the ingredient detail view
        request = self.factory.get(reverse('ingredient-detail', kwargs={'pk': self.ingredient1.pk}))
        response = ingredient_detail(request, pk=self.ingredient1.pk)
        self.assertIsInstance(response, HttpResponse)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.ingredient1._name)

        


