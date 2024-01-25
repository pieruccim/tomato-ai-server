from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Ingredient
from .forms import IngredientForm

# Create your views here.

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
