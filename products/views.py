from django.shortcuts import render,redirect

from django.http import request

from orders.models import Order
from products.models import Product
from .forms import ProductForm

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
    total_orders=Order.objects.all().count()
    context={'products':products,'total_orders':total_orders}
    return render(request,'products/index.html',context)





    
    
    


