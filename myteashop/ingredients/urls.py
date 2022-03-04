from django.urls import path
from ingredients import views

app_name = 'ingredients'

urlpatterns = [
    path('adaugare/', views.CreateIngredientsView.as_view(), name='adauga'),
    path('', views.IngredientsView.as_view(), name='lista_ingredients'),
    path('modificare/<int:pk>/', views.UpdateIngredientsView.as_view(), name='modifica'),
    path('sterge/<int:pk>/', views.deactivate_ingredients, name='dezactiveaza'),
    path('email/', views.sendanemail, name='email'),
]