from django.shortcuts import render,redirect

from django.http import request

from orders.models import Order
from products.models import Product
from .forms import ProductForm

from .filters import ProductFilter

# Create your views here.




def create(request):
    form=ProductForm()
 
    if(request.method=='POST'):
        form=ProductForm(request.POST)
        if(form.is_valid()):
            form.save()
            
        return redirect('/products/list?Product added ')
    
    return render(request,'products/create.html',{'form':form})
    


def index(request):
    products=Product.objects.all()
    myFilter = ProductFilter(request.GET,queryset=products)
    products = myFilter.qs
    '''
    -->like form we render filterform
    -->we use get because we see result on same page 
    -->quertset because we have to see filter data that we search
    -->
    -->qs = queryset
    '''


    context={'products':products,'myFilter':myFilter}
    return render(request,'products/index.html',context)





    
    
    


