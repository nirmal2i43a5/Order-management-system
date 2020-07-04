



from django import forms
from django.forms import ModelForm
from .models import Customer

# class CustomerForm(forms.Form):
 
#     full_name=forms.CharField(max_length=50,required=True)
#     email=forms.CharField(max_length=50,required=True)
#     contact=forms.CharField(max_length=50,required=True)
#     status=forms.BooleanField(required=False)
    
    # status=forms.BooleanField(required=False)
    
    
class CustomerModelForm(ModelForm):
    
    name=forms.CharField(widget=forms.TextInput(attrs={"placeholder": " Enter Full Name",}))
    email=forms.CharField(widget=forms.TextInput(attrs={"placeholder": " Enter Email",}))
    contact=forms.CharField(widget=forms.TextInput(attrs={"placeholder": " Enter Contact",}))
    class Meta:
        model=Customer
        fields=['name','email','contact']



 
 
 
    
        
        
     
        

    
    
    
    
    
    
    
    