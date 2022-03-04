from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView
from distributors.models import Distributors

class CreateDistributorsView(LoginRequiredMixin, CreateView):
    model = Distributors
    # fields = '__all__' # le afisam pe toate din models
    fields = ['distributor_name', 'city', 'country', 'email', 'phone'] # daca dorim sa numim doar anumite campuri pentru vizualizare
    template_name = 'distributors_form.html'

    def get_success_url(self):
        return reverse('distributors:lista_distributors')

class DistributorsView(LoginRequiredMixin, ListView):
    model = Distributors
    template_name = 'distributors_index.html'
    paginate_by = 5

    def get_queryset(self):
        return Distributors.objects.filter(active=True)

class UpdateDistributorsView(LoginRequiredMixin, UpdateView):
    model = Distributors
    # fields = '__all__'
    fields = ['distributor_name', 'city', 'country', 'email', 'phone']
    template_name = 'distributors_form.html'

    def get_queryset(self):
        return Distributors.objects.filter(active=True)

    def get_success_url(self):
        return reverse('distributors:lista_distributors')

@login_required
def deactivate_distributors(request, pk):
    if Distributors.objects.filter(id=pk).exists():
        Distributors.objects.filter(id=pk).update(active=False)
    return redirect('distributors:lista_distributors')