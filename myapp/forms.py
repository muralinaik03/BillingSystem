# forms.py
from django import forms
from .models import Product, ProductItem, Customer, Bill, BillItem
from django.forms import inlineformset_factory

class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=100)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class AddProductToBillForm(forms.Form):
    product = forms.ModelChoiceField(queryset=Product.objects.all(), label='Select Product')
    quantity = forms.IntegerField(min_value=1, label='Quantity')
    

class AddProductItemForm(forms.ModelForm):
    class Meta:
        model = ProductItem
        fields = ['product', 'quantity']
        
class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price']
        
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price']
        
class AddCustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone_number']
        
        
class BillForm(forms.ModelForm):
    class Meta:
        model = Bill
        fields = ['customer']
        
class BillItemForm(forms.ModelForm):
    class Meta:
        model = BillItem
        fields = ['product', 'quantity',]
        
ItemFormSet = inlineformset_factory(Bill, BillItem, form=BillItemForm, extra=1)