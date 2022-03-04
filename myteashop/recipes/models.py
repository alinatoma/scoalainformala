from django.db import models
from ingredients.models import Ingredient


class Recipe(models.Model):

    recipe_name =models.CharField(max_length=100)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    active = models.BooleanField(default=1)

    def __str__(self):
        return f"{self.recipe_name} - {self.quantity}"
