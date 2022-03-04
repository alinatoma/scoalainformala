from django.db import models
from distributors.models import Distributors


class Ingredient(models.Model):

    ingredient_name =models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    quantity = models.IntegerField()
    image_ingredient = models.ImageField(upload_to='ingredient_images/', null=True, default=None)
    distributor = models.ForeignKey(Distributors, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)
    active = models.BooleanField(default=1)

    def __str__(self):
        return f"{self.ingredient_name} - {self.quantity}"

    @property
    def image(self):
        if self.image_ingredient:
            return self.image_ingredient.url

        return static('images/defaultIngredient.jpg')