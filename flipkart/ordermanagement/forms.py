from django.forms import ModelForm
from .models import *
from django import forms

class Customer_form(forms.ModelForm):
    
    class Meta:
        model = Customer
        fields='__all__'
        
        widgets = {
            'customer_name' : forms.TextInput(attrs={'class' :'form-control'}),
            'customer_since' : forms.DateInput(attrs={'class' :'form-control'}),
        }   
    
class Order_form(forms.ModelForm):
    
    class Meta:
        model = Order
        fields = ['Customer_reference','product_reference','order_number','order_date','quantity']
        
        widgets = {
        
            'order_number' : forms.NumberInput(attrs={'class' :'form-control'}),
            'order_date' : forms.DateInput(attrs={'class' :'form-control'}),
            'quantity' : forms.NumberInput(attrs={'class' :'form-control'}),
            'price' : forms.NumberInput(attrs={'class' :'form-control'}),
            'gst' : forms.NumberInput(attrs={'class' :'form-control'}),
            'bill' : forms.NumberInput(attrs={'class' :'form-control'}),
        }   
    