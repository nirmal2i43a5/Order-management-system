

from django.contrib.auth.models import User,Group
from django.contrib.auth.forms import UserCreationForm,PasswordResetForm,AuthenticationForm
from django import forms
from django.forms import EmailField,TextInput,PasswordInput,ImageField
from .models import Profile
from django.utils.translation import ugettext_lazy as _ #for protected-


class LoginForm(AuthenticationForm):
	# email = EmailField(label=_("Email"), required=True,help_text=_("Required.")) #Email address is protected
	pass

	#although i write email field in models this field is compulsary for extra email authentication
	#if i want to add contact i can also add contact and other that should be in model
	
	#writing meta for this is optional
	# class Meta:
	#     model = User
	#     fields=('username','email','password')
		
   
class SignupForm(UserCreationForm):
	username=forms.CharField(widget=forms.TextInput(attrs={"placeholder": " Enter Username",}))
	email=forms.EmailField(widget=forms.TextInput(attrs={"placeholder": " Enter Email",}))
	password1=forms.CharField(widget=forms.TextInput(attrs={"placeholder": " Enter Password",'type' : 'password'}),label=_("Password"))
	password2=forms.CharField(widget=forms.TextInput(attrs={"placeholder": " Confirm Password",'type' : 'password'}),label=_("Confirm Password"))
	
 	#just using role i cannot see paarticular role for this i have to override __init__()=>look at below code
	role = forms.ModelChoiceField(queryset = Group.objects.all())

	
	class Meta:
		model = User
		fields = ('username','email','password1','password2',)#'__all__' also
		#email field is added later
		
		#help_text will remove the default text in signup page
		help_texts= {
			'username':None,
			# 'email':"Your email should contain @" if i add email and wants help_texts for that
		   #to remove help text of password and password2 go to UserCreationForm  and comment help_text in 
		}


	#this assists to show particular role while editing
	#  https://www.youtube.com/watch?v=Gb5ACR0jUyw&list=PL1WVjBsN-_NIdlnACz0Mxuq8VcuxER-is&index=19
	def __init__(self, *args, **kwargs):
		if kwargs.get('instance'):
      
			initial = kwargs.setdefault('initial', {})
   
			if kwargs['instance'].group.all():
				initial['role'] = kwargs['instance'].group.all()[0]#show this in first of choose form
    
			else:
				initial['role'] = None

		UserCreationForm.__init__(self,*args,**kwargs)
			
	

class UpdateDefaultProfile(forms.ModelForm):

	
	class Meta:
		model = User
		fields = ('username','email',)
	
	

			

class UpdateCustomProfile(forms.ModelForm):
	# role = forms.ModelChoiceField(queryset = Group.objects.all())
   
    	
	class Meta:
		model = Profile
		fields = ('fname','lname','address','contact','profile_img',)	
	

			
  
	
	
 