from django import forms
from django.core.exceptions import ValidationError
from .models import Products

class LoginForm(forms.Form):
    name = forms.CharField(max_length=100, label='Product Name')
    type = forms.CharField(max_length=100, label='Product Type')
    price = forms.DecimalField(min_value=0, label='Product Price')
    image = forms.ImageField(label='Product Image')

    def clean_name(self):
        name = self.cleaned_data['name']
        if Products.objects.filter(name__iexact=name).exists():
            raise ValidationError("This product name already exists.")
        return name

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError("Price cannot be negative.")
        return price