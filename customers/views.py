from django.shortcuts import render,redirect,get_object_or_404
from django.http import request
# from django.contrib.auth.decorators import login_required

from customers.models import Customer
from orders.models import Order
# from django.contrib.auth.models import User


from customers.forms import CustomerModelForm
from customers.filters import CustomerFilter
from django.contrib import messages
from django.views.generic import ListView #for pagination




'''
-->Before i use go to customers/create url to get form and use this create function separately but when i use j query i have to render form in same page.i.e customers/list
page.So,I only use index form as i render from there in context
def create(request):
    
    form=CustomerModelForm()
     
    if(request.method=='POST'):
        form=CustomerModelForm(request.POST)#form post ma show hunxa 
        if(form.is_valid()):
            form.save()
           
        return redirect('/customers/list?success')
    
            
    return render(request,'customers/create.html',{'form':form})#first ma yo page dekhinxa
'''


def index(request):
    form = CustomerModelForm()
    customers=Customer.objects.all()  
    myFilter = CustomerFilter(request.GET,queryset=customers)
    customers = myFilter.qs
    
    if request.method=='POST':
        form = CustomerModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/customers/list?customer added successfully')
            
    
    context={
        'customers':customers,'myFilter':myFilter,'form':form
        }
    return render(request,'customers/copindex.html',context)

#I use function base view but use class base view to inherit index.I am just copying index code 

# @login_required(login_url="/admin/login")

def edit(request, cid):    
    # cus=Customer.objects.get(id=pk) #i get all value and show that value to next page
    cus = get_object_or_404(Customer,pk = cid)
    form=CustomerModelForm(instance=cus)
    
    if(request.method=='POST'):
        form=CustomerModelForm(request.POST,instance=cus)
        if(form.is_valid()):
            form.save()
            messages.success(request, 'Customer record is successfully updated.',extra_tags='alert') #extra_tags assists uu to use alert
            
            return redirect('/customers/list/?edited-successfully')#maila update.html ko save garda or post ma jada yo url ma redirect hunxa
      
          



    # else:
    #     form = CustomerModelForm()
        
  
    return render(request,'customers/update.html',{'form':form})


def delete(request, cid):
    
    
    # cus=Customer.objects.get(id=pk)
    cus = get_object_or_404(Customer,pk = cid)
    
                                     # print(f'I am instance of {{cus}}')
   
    if request.method=='POST':  #if i confirm in delete.html page
        cus.delete()   #grab customer details and delete and after deleting moves to /customers/list/
     
        return redirect('customer_app:list')
    
    return render(request,'customers/delete.html',{'name':cus })#urls.py ko url render ma url search garxa at first


def cus_ord_view(request, cid):
    
    
    # order = Order.objects.filter(customer__first_name="Shankar") 
    # -->maila particular person ko order retrieve garaxu--
    
    customer = get_object_or_404(Customer,pk=cid) #use to get beautiful error -u can also use below
    # customer = Customer.objects.get(pk = cid)#return a particular name according to choosen primary key
  
    orders = customer.order_set.all()#particular customer ko particular order selct garxa
   
    order_count = orders.count()

    context = {'customer':customer, 'orders':orders, 'order_count':order_count}
 
    return render(request,'customers/orderview.html',context)

    
    


class CustomerPagination(ListView):
    model = Customer
    template_name = 'customers/copindex.html'  # Default: <app_label>/<model_name>_list.html
    context_object_name = 'customers'  # Default: object_list i.e contexxt i use in copindex.html--Customer.objects.all() ko data tanxa
    paginate_by = 10
    # queryset = Customer.objects.all()  # Default: Model.objects.all()
   





