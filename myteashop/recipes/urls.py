from django.urls import path
from recipes import views

app_name = 'recipes'

urlpatterns = [
    path('adaugare/', views.CreateRecipesView.as_view(), name='adauga'),
    path('', views.RecipesView.as_view(), name='lista_recipes'),
    path('modificare/<int:pk>/', views.UpdateRecipesView.as_view(), name='modifica'),
    path('preparare/<int:pk>/', views.prepare_recipes, name='prepara'),
    path('sterge/<int:pk>/', views.deactivate_recipes, name='dezactiveaza'),
]