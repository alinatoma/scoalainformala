from django.urls import path
from distributors import views

app_name = 'distributors'

urlpatterns = [
    path('adaugare/', views.CreateDistributorsView.as_view(), name='adauga'),
    path('', views.DistributorsView.as_view(), name='lista_distributors'),
    path('modificare/<int:pk>/', views.UpdateDistributorsView.as_view(), name='modifica'),
    path('sterge/<int:pk>/', views.deactivate_distributors, name='dezactiveaza'),
]