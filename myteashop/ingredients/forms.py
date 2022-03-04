from django import forms
from utils.upload import store_uploaded_file
from ingredients.models import Ingredient


class IngredientImageForm(forms.Form):
    image = forms.ImageField(label='Image to upload', required=True)

    def save(self):
        image = self.cleaned_data.get('image')
        store_uploaded_file(image)

class IngredientImageForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = ['image_ingredient']

class EmailForm(forms.Form):
    recipient = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
