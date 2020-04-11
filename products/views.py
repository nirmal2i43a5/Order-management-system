from django.shortcuts import render,redirect,get_object_or_404

from django.http import request,JsonResponse
from django.template.loader import render_to_string

from orders.models import Order
from products.models import Product
from .forms import ProductForm

from .filters import ProductFilter

from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger






# def create(request):
#     form=ProductForm()
 
#     if(request.method=='POST'):
#         form=ProductForm(request.POST)
#         if(form.is_valid()):
#             form.save()
            
#         return redirect('/products/list?Product added ')
    
#     return render(request,'products/create.html',{'form':form})
    


def index(request):   
    form = ProductForm()
    products=Product.objects.all()
    product_count = products.count()
    
    myFilter = ProductFilter(request.GET,queryset=products)
    products = myFilter.qs
    
    '''
    -->like form we render filterform
    -->we use get because we see result on same page 
    -->quertset because we have to see filter data that we search
    -->
    -->qs = queryset
    '''
    page = request.GET.get('page', 1)#means page  number 1
    
    # if page and page.isdigit():
    #     page = int(page)
    # else:
    #     page = 5
        
    # paginator = Paginator(customers, 5)#5 data per page
    paginator = Paginator(products, 10)
  
    try:
        products = paginator.page(page)
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        #if page is out of range show last page
        products = paginator.page(paginator.num_pages)

    if(request.method=='POST'):
        form=ProductForm(request.POST)
        if(form.is_valid()):
            form.save()
            
        # return redirect('/products/list?Product added ')    
    context={'products':products,
             'myFilter':myFilter,
             'form':form,
             'start':products.start_index(),
             'end':products.end_index(),
             'products_count':product_count
             }
    return render(request,'products/index.html',context)






def save_product_form(request, form, template_name):
   
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            products = Product.objects.all()
            data['html_product_list'] = render_to_string('products/index.html', {
                #valid huda data goes to index.html else stay on template_name
                'products': products
            })
          
            
        else:
            data['form_is_valid'] = False
            
    context = {'form': form}
    data['html_form'] = render_to_string(template_name, context, request=request)
    
    return JsonResponse(data)

def create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
    else:
        form = ProductForm()   
    return save_product_form(request,form,'products/create.html')



def edit(request, pid):
   
    pro = get_object_or_404(Product, pk=pid)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=pro)
        
    else:
        
        form = ProductForm(instance=pro)
    return save_product_form(request, form, 'products/update.html')


def delete_product(request, pid):
    data = dict()
    product = get_object_or_404(Product, pk=pid)
    
    if(request.method == 'POST'):#Use this when i confirm delete 
       
        product.delete()
        
        data['form_is_valid'] = True
        products = Product.objects.all()
        data['html_product_list'] = render_to_string('products/index.html',{'products':products})   
        
    else:
        
        context = {'pro': product}#this goes to action pro.id in delete.html
        data['html_form'] = render_to_string('products/delete.html', context, request=request)
    
    
    return JsonResponse(data)




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









    
    
    


