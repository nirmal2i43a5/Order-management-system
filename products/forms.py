
from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        # fields=['name','price','category','description']
        fields = '__all__'
        exclude = ('category',)
    
        
    #i dont need to write form.CharField to show form only but to show design i need
   
   
   
    ''' name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'input',
            
            'class':'form-control',
            'class':'col-md-6',
            # # 'class':'form-group',
            'placeholder':'Enter Product Name'
            
        } ))
    
    price = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'class':'col-md-6',
            # 'class':'form-group',
            'placeholder':'Enter Price'
        }     ))
    
    # category = forms.CharField(widget=forms.TextInput(
    #     attrs={
    #         'class':'form-control',
    #         'class':'col-md-6',
    #         # 'class':'form-group',
        
    #     }     ))
    
    description = forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            'class':'col-md-6',
            # 'class':'form-group',
            'placeholder':'Describe Product'
        }     ))
 '''
   