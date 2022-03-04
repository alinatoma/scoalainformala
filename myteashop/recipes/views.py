from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView
from recipes.models import Recipe
from ingredients.models import Ingredient


class CreateRecipesView(LoginRequiredMixin, CreateView):
    model = Recipe
    # fields = '__all__' # le afisam pe toate din models
    fields = ['recipe_name', 'ingredient', 'quantity']  # daca dorim sa numim doar anumite campuri pentru vizualizare
    template_name = 'recipes_form.html'

    def get_success_url(self):
        return reverse('recipes:lista_recipes')


class RecipesView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'recipes_index.html'
    paginate_by = 5

    def get_queryset(self):
        return Recipe.objects.filter(active=True)


class UpdateRecipesView(LoginRequiredMixin, UpdateView):
    model = Recipe
    # fields = '__all__'
    fields = ['recipe_name', 'ingredient', 'quantity']
    template_name = 'recipes_form.html'

    def get_queryset(self):
        return Recipe.objects.filter(active=True)

    def get_success_url(self):
        return reverse('recipes:lista_recipes')



@login_required
def deactivate_recipes(request, pk):
    if Recipe.objects.filter(id=pk).exists():
        Recipe.objects.filter(id=pk).update(active=False)
    return redirect('recipes:lista_recipes')


@login_required
def prepare_recipes(request, pk):
    if Recipe.objects.filter(id=pk).exists():
        recipe_instance = Recipe.objects.get(id=pk)
        recipe_quantity = recipe_instance.quantity
        ingredient = Ingredient.objects.get(id=pk)
        quantity = ingredient.quantity
        Ingredient.objects.filter(id=ingredient.id).update(quantity=quantity - recipe_quantity)
    return redirect('recipes:lista_recipes')


