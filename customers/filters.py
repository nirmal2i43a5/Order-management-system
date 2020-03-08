

#Before you make filters.py you have to add 'django_filters' in INSTALLED_APPS and then pip install django_filter
import django_filters 
from django_filters import DateFilter,CharFilter
#import CharFilter only when you want to search with single or more character
from customers.models import Customer


class CustomerFilter(django_filters.FilterSet):
    
    # start_date = DateFilter(field_name="created_at",lookup_expr='gte')
    
    '''
    Date range filter
    # lookup_expr gives the result in which data is greater or equal to given date
    # gte=greater than equals--created_at is my models of Product
    '''
    
    # end_date = DateFilter(field_name="created_at",lookup_expr='lte')#lte=less than equals
    
    first_name = CharFilter(field_name="first_name",lookup_expr='icontains')
    # --->icontains means igonring casesensitive
    #u--->sing this i can search even with single character
    
    
    class Meta:
        model = Customer#make filter for model Customer
        
        fields = ('first_name',)#generate filter form with all first_name
       