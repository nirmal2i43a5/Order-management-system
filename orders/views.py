from django.shortcuts import render,redirect,get_object_or_404,reverse

from django.http import JsonResponse
from .models import Order,Customer,Product
from orders.forms import OrderForm
from orders.filters import OrderFilter
from django.forms import inlineformset_factory#It brings multiple form in group
from django.contrib import messages

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.db.models import Q

from django.template.loader import render_to_string





def create(request,cid):
    '''Below I replace OrderForm with'''
    
    OrderFormSet = inlineformset_factory(Customer,Order,fields='__all__',exclude=('total_price',),extra=1)  
    #it means maila customer lai click garda order ma bhako detail access garako xu with instance
     #parent model and then child model---
    #we can have multiple order so we need to tell which to allow by fields
   
    cus = Customer.objects.get(pk=cid)
    formset = OrderFormSet(queryset=Order.objects.none(),instance=cus)
    #queryset =Order.objects.none() la --> already bhako product inline form ma show hudaina maila Add order ma jada
    # form = OrderForm(initial={'customer':cus})#right customer is in model--comment this wh
    
    if request.method=='POST':
        # form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST,instance=cus)
        if formset.is_valid():
            formset.save()
        return redirect('customer_app:view', cid)
    
    return render(request,'orders/create.html',{'formset':formset})

def index(request):
    
    orders=Order.objects.all()
    
    total_orders=orders.count()
    # myFilter = OrderFilter(request.GET,queryset=orders)
    # orders = myFilter.qs
    # # customers=Customer.objects.all()
  
    pending=orders.filter(status='Pending').count()#filter la choose(search)  garxa and all pending lai count garxa
    delivered=orders.filter(status="Delivered").count()
    
    
       
    page = request.GET.get('page', 1)#means page  number 1
    paginator = Paginator(orders, 5)
  
    try:
        orders = paginator.page(page)
    except PageNotAnInteger:
        orders = paginator.page(1)
    except EmptyPage:
        #if page is out of range show last page
        orders = paginator.page(paginator.num_pages)

    
    if request.method=='POST':
        form = CustomerModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/customers/list?customer added successfully')
            
    context={
        'orders':orders,'total_orders':total_orders,
        'orders_pending':pending,'orders_delivered':delivered,
        # 'myFilter':myFilter,
        'start':orders.start_index(),
        'end':orders.end_index()
        
        }
    return render(request,'orders/index.html',context)


def search(request):
    data = dict()
    field_value = request.GET.get('query')
    print(field_value)
    
    # products = Product.objects.all()
    # myFilter = ProductFilter(request.GET,queryset=products)
    # products = myFilter.qs
  
  
    if field_value:
        orders = Order.objects.filter(
                                            Q(product__name__contains=field_value)
                                           |Q(status__icontains=field_value) 
                                           | Q(total_price__contains=field_value)
                                           | Q(quantity__contains=field_value)
                                            | Q(customer__name__contains=field_value)
                                             
                                        
                                           )
        
        

        context = {'orders': orders}
            
        data['html_list'] = render_to_string('orders/get_search_orders.html',context,request=request)
        return JsonResponse(data)

    else:
        orders = Order.objects.all()
       
        context = {'orders': orders}
        data['html_list'] = render_to_string('orders/get_search_orders.html',context,request=request)

        return JsonResponse(data)


def edit(request, oid):    
    # ord=Order.objects.get(pk=oid) #i get all value and show that value to next page
    
    ord = get_object_or_404(Order,pk = oid)
    
    form=OrderForm(instance=ord)
    
    # cus = get_object_or_404(Customer,pk = cid)
   
    
    if(request.method=='POST'):
        
        form=OrderForm(request.POST,instance=ord)
        if(form.is_valid()):
            form.save()
            messages.success(request,'Order is successfully updates.',extra_tags='alert')
            
            return redirect('order_app:list')
            
            # return redirect("/customers/order/", pk = cid)#maila update.html ko save garda or post ma jada yo url ma redirect hunxa

    # else:
    #     form = ProductForm()
        
  
    return render(request,'orders/update.html',{'form':form})


def delete(request, oid):
        # cus=Customer.objects.get(id=pk)
    ord = get_object_or_404(Order,pk = oid) 
    if request.method=='POST':#if i confirm in delete.html page
        ord.delete()   #grab customer details and delete and after deleting moves to /customers/list/
        return redirect('order_app:list')
    
    return render(request,'orders/delete.html',{'name':ord})#urls.py ko url render ma url search garxa at first

