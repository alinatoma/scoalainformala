from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView, ListView, UpdateView
from ingredients.models import Ingredient
from django.core.mail import send_mail
from django.conf import settings
from ingredients.forms import EmailForm


class CreateIngredientsView(LoginRequiredMixin, CreateView):
    model = Ingredient
    # fields = '__all__' # le afisam pe toate din models
    fields = ['ingredient_name', 'description', 'quantity', 'image_ingredient', 'distributor'] # daca dorim sa numim doar anumite campuri pentru vizualizare
    template_name = 'ingredients_form.html'

    def upload_view(request):
        if request.method == 'GET':
            form = IngredientImageForm()
        else:
            form = IngredientImageForm(request.POST, request.FILES)

            if form.is_valid():
                form.save()

                return render(request)

        return render(request, 'ingredients/upload.html', {
            'form': form
        })

    def get_success_url(self):
        return reverse('ingredients:lista_ingredients')

class IngredientsView(LoginRequiredMixin, ListView):
    model = Ingredient
    template_name = 'ingredients_index.html'
    paginate_by = 5

    def get_queryset(self):
        return Ingredient.objects.filter(active=True)

class UpdateIngredientsView(LoginRequiredMixin, UpdateView):
    model = Ingredient
    # fields = '__all__'
    fields = ['ingredient_name', 'description', 'quantity', 'image_ingredient', 'distributor']
    template_name = 'ingredients_form.html'

    def get_queryset(self):
        return Ingredient.objects.filter(active=True)

    def get_success_url(self):
        return reverse('ingredients:lista_ingredients')

@login_required
def deactivate_ingredients(request, pk):
    if Ingredient.objects.filter(id=pk).exists():
        Ingredient.objects.filter(id=pk).update(active=False)
    return redirect('ingredients:lista_ingredients')


@login_required
def sendanemail(request):

    # create a variable to keep track of the form
    messageSent = False

    # check if form has been submitted
    if request.method == 'POST':

        form = EmailForm(request.POST)

        # check if data from the form is clean
        if form.is_valid():
            cd = form.cleaned_data
            subject = "Sending new order"
            message = cd['message']

            # send the email to the recipent
            send_mail(subject, message,
                      settings.DEFAULT_FROM_EMAIL, [cd['recipient']])

            # set the variable initially created to True
            messageSent = True

    else:
        form = EmailForm()

    return render(request, 'email_template.html', {

        'form': form,
        'messageSent': messageSent,

    })