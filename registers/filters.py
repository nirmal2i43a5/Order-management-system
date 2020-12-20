import django_filters
from django_filters import DateFilter, CharFilter

from customers.models import Customer
from django.forms.widgets import TextInput,DateInput

from django import forms

#this is for datepicker
class DateInput(forms.DateInput):
    input_type = 'date'
    
class CustomerFilter(django_filters.FilterSet):
	# start_date = DateFilter(field_name="date_created", lookup_expr='gte',label="",
    #                      widget=DateInput(attrs={'placeholder': ' Data >  =   (YYYY-MM-DD)'}))
	start_date = DateFilter(field_name="date_created", lookup_expr='gte',label="",
	widget=DateInput())

	end_date = DateFilter(field_name="date_created", lookup_expr='lte',label="",widget=DateInput())
	# note = CharFilter(field_name='note', lookup_expr='icontains')


	class Meta:
		model = Customer
		fields = '__all__'
		exclude = ('date_created','email','name','contact',)
  
  


	