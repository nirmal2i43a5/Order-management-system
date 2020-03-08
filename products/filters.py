

#Before you make filters.py you have to add 'django_filters' in INSTALLED_APPS and then pip install django_filter
import django_filters 
from django_filters import DateFilter,CharFilter
#import CharFilter only when you want to search with single or more character


from products.models import Product
from django.forms import DateInput

class ProductFilter(django_filters.FilterSet):
    
    # start_date = DateFilter(field_name="created_at",lookup_expr='gte')
    
    '''
    Date range filter
    # lookup_expr gives the result in which data is greater or equal to given date
    # gte=greater than equals--created_at is my models of Product
    '''
    
    # end_date = DateFilter(field_name="created_at",lookup_expr='lte')#lte=less than equals
    # name = django_filters.DateFilter(widget=DateInput(attrs={'class':'datepicker','placeholder':'Search for ...'}))
    
    name = CharFilter(field_name="name",lookup_expr='icontains')
    # --->icontains means igonring casesensitive
    #u--->sing this i can search even with single character
    
    
    class Meta:
        model = Product#make filter for model Product
        
        fields = '__all__'#generate filter form with all models
        exclude = ['created_at','description','category','price']