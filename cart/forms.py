from django import forms
from django.forms import fields
from .models import OrderItem


class AddToCartForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['quantity']