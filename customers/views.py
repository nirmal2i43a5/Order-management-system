from django.shortcuts import render,redirect,get_object_or_404
from django.http import request,JsonResponse
from django.core import serializers
# from django.contrib.auth.decorators import login_required

from customers.models import Customer
from orders.models import Order
from products.models import Product
# from django.contrib.auth.models import User

from django.contrib import messages
from customers.forms import CustomerModelForm
from customers.filters import CustomerFilter
from django.contrib import messages
from django.utils import timezone
from django.views.generic import ListView,DetailView#for pagination
from django.views.generic import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.template.loader import render_to_string

from django.db.models import Q
from django.contrib.auth.decorators import login_required


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
			
		
@login_required(login_url = '/user/login/')     
def index(request):
	form = CustomerModelForm()
	customers=Customer.objects.all().order_by("-id")
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
	paginator = Paginator(customers, 10)
  
	try:
		customers = paginator.page(page)
	except PageNotAnInteger:
		customers = paginator.page(1)
	except EmptyPage:
		#if page is out of range show last page
		customers = paginator.page(paginator.num_pages)

	

	context={
		'customers':customers,#this is for both pagination and table list use(blc table list also should support pagination.so dont pass data for list separately)
  		
		'myFilter':myFilter,
		'form':form,'page':page,
		'customer_count':customer_count,
		'start': customers.start_index(),
		'end': customers.end_index(),
		}
	return render(request,'customers/copindex.html',context)



#I use function base view but use class base view to inherit index.I am just copying index code 
def search(request):
	data = dict()
	field_value = request.GET.get('query')#grab the input value
	print(field_value)
	
	# products = Product.objects.all()
	# myFilter = ProductFilter(request.GET,queryset=products)
	# products = myFilter.qs
 
	if field_value:
		customers = Customer.objects.filter(
	  
											Q(name__contains=field_value)
										   |Q(email__icontains=field_value) 
										   | Q(contact__contains=field_value)  
										   |Q(date_created__contains=field_value)                      
										   )
	
		context = {'customers': customers}
		data['html_list'] = render_to_string('customers/get_search_customers.html',context,request=request)
		return JsonResponse(data)
	else:
		customers = Customer.objects.all()
		context = {'customers': customers}
		data['html_list'] = render_to_string('customers/get_search_customers.html',context,request=request)
		return JsonResponse(data)





def create(request):    
	if request.method=="POST":
		form=CustomerModelForm(request.POST)
		if form.is_valid():
			cid =request.POST['cusid']
			name=request.POST.get("name")
			email=request.POST.get("email")
			contact=request.POST.get("contact")
		  
			
			if(cid==''):
				customer=Customer(name=name,email=email,contact=contact)
			else:
				customer=Customer(id = cid,name=name,email=email,contact=contact)
				
			customer.save()
			prod=Customer.objects.values()
			# print(prod,"--------------------------")
			customer_data =list(prod)
			
			return JsonResponse({'status':'Save','customer_data':customer_data,'message':'Customer is successfully submitted'},safe=False)
		else:
			return JsonResponse({'status':0},safe=False)
	   
  

def edit(request):
	if request.method=="POST":
		id=request.POST.get('cid')
		print(id)
		customer=Customer.objects.get(pk=id)
		customer_data={"id":customer.id,"name":customer.name,"email":customer.email, "contact":customer.contact}
	
		return JsonResponse(customer_data,safe=False)


	
def delete(request):
	if request.method=="POST":
		id=request.POST.get('cid')
		pi=Customer.objects.get(pk=id)
		pi.delete()
	  
		return JsonResponse({'status':1,'message':'Customer is successfully deleted'},safe=False)
	else:
		return JsonResponse({'status':0,'message':'Failed to delete data'},safe=False) 

   


def cus_ord_view(request, cid):
	# order = Order.objects.filter(customer__first_name="Shankar") 
	# -->I am retrieving  the order the  particular person 
 
	customer = get_object_or_404(Customer,pk=cid) #use to get beautiful error -u can also use below
	# customer = Customer.objects.get(pk = cid)#return a particular customer name according to choosen primary key
	orders = customer.order_set.all()#particular customer ko particular order select garxa--It is possible with customer id
	#here order in  order_set is attribute 
	#Order ma Customer is foreign key so ot os possible to use order_set with customer
	order_count = orders.count()
	order_count = orders.count()    
	customer_total_order_price=0.00
	
	for order in customer.order_set.all():
		per_total_price = float(order.product.price) * order.quantity
		# customer.per_total = per_total_price--to get the price of respective products
		#return value of first product i.e first row
		customer_total_order_price += per_total_price
		
	
 
	context = {'customer_total_price':customer_total_order_price,'customers':customer, 'orders':orders, 'order_count':order_count,'order_num':order_count}
	return render(request,'customers/orderview.html',context)

	
  
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
	
	
	


import calendar
from datetime import datetime,timedelta
from django.db.models.functions import TruncMonth,ExtractMonth
from django.db.models import Count,Sum

def customerChart(request):
	data = []
	last_month = datetime.now() - timedelta(days=30)
 
	#TruncDate allows you to group by date (day of month) #using TruncDate give me database time error so i use ExtractMonth
	#values is for grouping data
 
	customer = Customer.objects.\
	annotate(month=ExtractMonth('date_created')).\
	values('month').\
	annotate(customer_count=Count('id')).\
	values('month', 'customer_count').order_by()
	#month=ExtractMonth('date_created')) => month is the look_up name in ExtractMonth which is default
 	# Group By month and customer_count
	# Count('id') is used to count customer from their pk = id
	#I can also use ExtractYear and other in same logic and gives value as values('month','year')

	# print(list(customer))
	"""
	[{'month': 7, 'customer_count': 6}, {'month': 6, 'customer_count': 5}, {'month': 4, 'customer_count': 10}, {'month': 3, 'customer_count': 1}, {'month': 5, 'customer_count': 1}, {'month': 11, 'customer_count': 8}, {'month': 12, 'customer_count': 3}]
	"""
	
 	# customer = (Customer.objects\
	# 	.filter(date_created__gt=last_month).extra(select={'day':'date(date_created)'}).values('day').annotate(customer_count=Count('id')).order_by())       

	for cus in customer:
		# data.append({cus['month']:cus['customer_count']})this only give month number 
		data.append({calendar.month_name[cus['month']]:cus['customer_count']})
  
	# print(data)	
 
 	#[{7: 6}, {6: 5}, {4: 10}, {3: 1}, {5: 1}, {11: 8}, {12: 3}]#result with month number
	# [{"July": 6}, {"June": 5}, {"April": 10}, {"March": 1}, {"May": 1}, {"November": 8}, {"December": 3}]#with month name
	
	return JsonResponse(data,safe=False)
  
	

	
	
