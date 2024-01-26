from django.db import models

class Ingredient(models.Model):
    _ingredient_id = models.AutoField(primary_key=True)
    _name = models.CharField(max_length=100)

    @property
    def ingredient_id(self):
        return self._ingredient_id

    @property
    def name(self):
        return self._name
    
    def __str__(self):
        return self.name
    

class Restaurant(models.Model):
    _restaurant_id = models.AutoField(primary_key=True)
    _name = models.CharField(max_length=200)
    _location = models.CharField(max_length=255)

    @property
    def restaurant_id(self):
        return self._restaurant_id

    @property
    def name(self):
        return self._name

    @property
    def location(self):
        return self._location
    
    def __str__(self):
        return self.name
    

class Recipe(models.Model):
    _recipe_id = models.AutoField(primary_key=True)
    _title = models.CharField(max_length=200)
    _ingredients = models.ManyToManyField(Ingredient)
    _instructions = models.TextField()
    _restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)

    @property
    def recipe_id(self):
        return self._recipe_id

    @property
    def title(self):
        return self._title

    @property
    def ingredients(self):
        return self._ingredients.all()

    @property
    def instructions(self):
        return self._instructions

    @property
    def restaurant(self):
        return self._restaurant
    
    def __str__(self):
        return self.title

