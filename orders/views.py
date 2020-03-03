from django.shortcuts import render

from .models import Order
from orders.forms import OrderForm

# Create your views here.



def create(request):
    form = OrderForm()
    return render(request,'orders/create.html',{'form':form})

def index(request):#customer order index
    
    return render(request,'orders/index.html')