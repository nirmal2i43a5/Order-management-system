from django.shortcuts import render,redirect,get_object_or_404
from django.http import request
# from django.contrib.auth.decorators import login_required

from customers.models import Customer
from orders.models import Order
from products.models import Product
# from django.contrib.auth.models import User


from customers.forms import CustomerModelForm
from customers.filters import CustomerFilter
from django.contrib import messages
from django.utils import timezone
from django.views.generic import ListView,DetailView#for pagination
from django.views.generic import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger




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

# class CustomerPagination(ListView,DetailView):
#     model = Customer
#     # queryset = Customer.objects.all()--if I write i dont need to write query set ---use either
#     template_name = 'customers/copindex.html'  # Default: <app_label>/<model_name>_list.html
#     context_object_name = 'customers' #retrieve data from database
#      # Default: object_list i.e contexxt i use in copindex.html--Customer.objects.all() ko data tanxa
#     paginate_by = 5
#     ordering = ['-created_at']#Suppose you want the books whhile concerning with the book to be ordered in the page by their created date descending.
#      # Default: Model.objects.all()
    
   
# this is the class based view
# class IndexView(CustomerPagination,View):
    
    # def get(self,request,*args,**kwargs):
    #     form = CustomerModelForm()
    #     customers=Customer.objects.all()  
    #     myFilter = CustomerFilter(request.GET,queryset=customers)
    #     customers = myFilter.qs
    #     context={
    #     'customers':customers,'myFilter':myFilter,'form':form
    #     }
       
    #     return render(request,'customers/copindex.html',context)
    
    # def post(self,request,*args,**kwargs):
    #     form = CustomerModelForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #     return redirect('/customers/list?customer added successfully')
            
        
        
def index(request):
    form = CustomerModelForm()
    customers=Customer.objects.all()  
    myFilter = CustomerFilter(request.GET,queryset=customers)
    customers = myFilter.qs#for searchng
    
    #pagination logic
    customer_count = customers.count()
      

       
    page = request.GET.get('page', 1)#means page  number 1
    
    # if page and page.isdigit():
    #     page = int(page)
    # else:
    #     page = 5
        
    # paginator = Paginator(customers, 5)#5 data per page
    paginator = Paginator(customers, 5)
  
    try:
        customers = paginator.page(page)
    except PageNotAnInteger:
        customers = paginator.page(1)
    except EmptyPage:
        #if page is out of range show last page
        customers = paginator.page(paginator.num_pages)

    
    if request.method=='POST':
        form = CustomerModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/customers/list?customer added successfully')
            
    
    context={
        'customers':customers,'myFilter':myFilter,'form':form,'page':page,'customer_count':customer_count,
        'start': customers.start_index(),
        'end': customers.end_index(),
        }
    return render(request,'customers/copindex.html',context)



#I use function base view but use class base view to inherit index.I am just copying index code 


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
    # customer = Customer.objects.get(pk = cid)#return a particular customer name according to choosen primary key
  
    orders = customer.order_set.all()#particular customer ko particular order select garxa--ot is possible with customer id
    #here order in  order_set is attribute 
    #Order ma Customer is foreign key so ot os possible to use order_set with customer
   
    order_count = orders.count()    
    new_total=0.00
    for order in customer.order_set.all():
        per_total_price = float(order.product.price) * order.quantity
        # customer.per_total = per_total_price--to get the price of respective products
        #return value of first product i.e first row
        new_total += per_total_price
        
    customer.total = new_total#in orderview.html Total : {{customer.total}}--is the fianl result after loop completes
    customer.save()
    context = {'customer':customer, 'orders':orders, 'order_count':order_count}
 
    return render(request,'customers/orderview.html',context)

    
    

# @login_required
def add_to_cart(request, slug):
    product = get_object_or_404(Product, slug=slug)
    order_item, created = Order.objects.get_or_create(
        item=item,
        user=request.user,
        ordered=False
    )
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    if order_qs.exists():
        order = order_qs[0]
        # check if the order item is in the order
        if order.items.filter(product__slug=product.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "This item quantity was updated.")
            return redirect("/customers/products/")
        else:
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect("/customers/products/")
    else:
        ordered_date = timezone.now()
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.items.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect("core:order-summary")


def remove_single_item_from_cart(request, cid):
 
    product = get_object_or_404(Product, pk=cid)  
    customer = get_object_or_404(Customer,pk=cid)     
    for order_item in customer.order_set.all(): 
        order_item.quantity -= 1
        order_item.save()
    
    # if order_item.quantity > 1:#if quantity o then remove product
    
            
    # else:
    #     order.items.remove(order_item)
        messages.info(request, "This item quantity was updated.")
        return redirect("/customers/orders/",id = cid)
            
        
        
   
                
        
        
        
       
            
            
           
    #     else:
    #         messages.info(request, "This item was not in your cart")
    #         return redirect("/customers/orders/",pk = cid)
    # else:
    #     messages.info(request, "You do not have an active order")
    #     return redirect("/customers/orders/",pk = cid)

        
        
    
    
    # order_item = get_object_or_404(Order, pk=cid)
    # if order_item.quantity > 1:
    #     order_item.quantity -= 1
    #     order_item.save()
                
    # else:
    #     order.Order.remove(order_item)
        
        
    # messages.info(request, "This item quantity was updated.")
    # return redirect("/customers/orders/",pk = cid)
    
    
    
    
 

   





