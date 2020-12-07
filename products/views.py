from django.shortcuts import render,redirect,get_object_or_404

from django.http import request,JsonResponse
from django.template.loader import render_to_string

from orders.models import Order
from products.models import Product
from customers.models import Customer
from .forms import ProductForm
from django.contrib import messages
from .filters import ProductFilter

from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q,Sum
from django.contrib.auth.decorators import login_required



@login_required(login_url = '/user/login/')
def index(request):   
    form = ProductForm()
    products=Product.objects.all()#show the list
    product_count = products.count()
    
    products = getPaginator(request,products)
    '''
    -->like form we render filterform
    -->we use get because we see result on same page 
    -->quertset because we have to see filter data that we search
    -->
    -->qs = queryset
    '''
  

  
    context={'products':products,##this is for both pagination and table list use(blc table list also should support pagination.so dont pass data for list separately)
           
           
             'form':form,
             'start':products.start_index(),
             'end':products.end_index(),
             'products_count':product_count
             }
    return render(request,'products/index.html',context)



def getPaginator(request,object):
    page = request.GET.get('page', 1)#means page  number 1
    paginator = Paginator(object, 5)
  
    try:
        products = paginator.page(page)
        
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        #if page is out of range show last page
        products = paginator.page(paginator.num_pages)
        
    return products#aflter pagination return object


    
def search(request):
    data = dict()
    field_value = request.GET.get('query')
    print(field_value)
    
    # products = Product.objects.all()
    # myFilter = ProductFilter(request.GET,queryset=products)
    # products = myFilter.qs
  
  
    if field_value:
        products = Product.objects.filter(
                                            Q(name__icontains=field_value)
                                           | Q(price__icontains=field_value) 
                                           | Q(description__icontains=field_value)
                                           | Q(quantity__icontains=field_value)
                                           | Q(id__icontains=field_value)
                                           | Q(category__icontains=field_value)
                                           |Q(created_at__contains=field_value)
                                           )

        context = {'products': products}
            
        data['html_list'] = render_to_string('products/get_search_products.html',context,request=request)

   

        return JsonResponse(data,safe=False)

    else:
        products = Product.objects.all()
       
        context = {'products': products}
        data['html_list'] = render_to_string('products/get_search_products.html',context,request=request)

        return JsonResponse(data)



def create(request):  #get form is alreasy generated from index view above 
   
    if request.method=="POST":
        form=ProductForm(request.POST)
        if form.is_valid():
            pid =request.POST["proid"]#this is hidden field 
            name=request.POST.get("name")
            price=request.POST.get("price")
            quantity=request.POST.get("quantity")
            unit=request.POST.get("unit")
            description=request.POST.get("description")
            
            if(pid==''):#if there is no product id then it has to insert data clicking on save button
                product=Product(name=name,price=price,quantity=quantity,unit=unit,description=description)
                
            else:#if not id then edit data clicking on save button 
                product=Product(id = pid,name=name,price=price,quantity=quantity,unit=unit,description=description)
                
            product.save()#save when form is empty and i need to insert data
            prod=Product.objects.values()
            product_data =list(prod)
            return JsonResponse({'status':'Save','product_data':product_data,'message':'Product is successfully submitted'},safe=False)
        else:
            return JsonResponse({'status':0})
       
  

    
    
def edit(request):
    print("edit is click ----------------------")
    if request.method=="POST":
        id=request.POST.get('pid')
        # print(id)
        product=Product.objects.get(pk=id)
        product_data={"id":product.id,"name":product.name,"price":product.price,
                      "quantity":product.quantity,"unit":product.unit,"description":product.description}
    
        return JsonResponse(product_data)
    
    
    
    
def delete(request):
    if request.method=="POST":
        id=request.POST.get('pid')
        pi=Product.objects.get(pk=id)
        pi.delete()
      
        return JsonResponse({'status':1,'message':'Product is successfully deleted'},safe=False)
    else:
        return JsonResponse({'status':0,'message':'Failed to delete data'},safe=False)    




def productData(request,cid):
    
    productData = []
    cus = Customer.objects.get(pk=cid)
    # # customers = cus.values('name','created_at')

    order = cus.order_set.all()
    # order =  Order.objects.values('created_at','product__price')
    # productData = serializers.serialize('json',order)
    # productData = productData['name']
    
    
    for i in order:
        productData.append({i.customer.name:i.product.price})#right is value(can be value or string) and left(always string cannot be number) is keys in dict 
        # Date.append(i['created_at'])
        # productPrice.append(i['product__price'])
     
    print(productData)
    return JsonResponse(productData,safe=False)









# ------------------------------------------------------------------------------------------------------------------------------------
'''

def delete(request, pid):
 # cus=Customer.objects.get(id=pk)
    pro = get_object_or_404(Product,pk = pid)
    
                                     # print(f'I am instance of {{cus}}')
   
    if request.method=='POST':  #if i confirm in delete.html page otherwise dont need post request
        pro.delete()   #grab customer details and delete and after deleting moves to /customers/list/
     
        return redirect('product_app:list')
    
    return render(request,'products/delete.html',{'name':pro })#urls.py ko url render ma url search garxa at first




def edit(request, pid):    
    # pro=Product.objects.get(id=pk) #i get all value and show that value to next page
    pro = get_object_or_404(Product,pk = pid)
    form=ProductForm(instance=pro)
    
    if(request.method=='POST'):
        
        form=ProductForm(request.POST,instance=pro)
        if(form.is_valid()):
            form.save()
            messages.success(request,'Product is successfully updated.',extra_tags='alert')
            
        return redirect('product_app:list')#maila update.html ko save garda or post ma jada yo url ma redirect hunxa

    # else:
    #     form = ProductForm()
        
  
    return render(request,'products/update.html',{'form':form})
    
    '''
    
    
    









    
    
    


