from django import forms
from django.forms import fields

from cart.models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product

        fields = ['title', 'image', 'description', 'price', 'available_colours', 'available_sizes']