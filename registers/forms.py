

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django import forms

class SignupForm(UserCreationForm):
    # email = forms.CharField() maila add garako
    
    class Meta:
        model = User
        fields = ('username','password1','password2')#default
        
        #help_text will remove the default text in signup page
        help_texts= {
            'username':None,
            # 'email':"Your email should contain @" if i add email and wants help_texts for that
           #to remove help text of password and password2 go to UserCreationForm  and comment help_text in 
        }