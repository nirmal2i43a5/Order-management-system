from django import forms

from .models import Order,Product,Customer

# from products.models import Product
# from customers.models import Customer


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields='__all__'