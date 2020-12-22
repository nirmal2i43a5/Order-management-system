from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, reverse, redirect, resolve_url

# from django.http import HttpResponseRedirect
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.views.generic import CreateView

from .forms import SignupForm, UpdateDefaultProfile, UpdateCustomProfile
from django.contrib import messages
from customers.models import Customer
from orders.models import Order
from registers.models import Profile
from products.models import Product, HistConf
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.http import HttpResponse, HttpResponseRedirect
import json

from django.views.generic import DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from registers.filters import CustomerFilter
from django.contrib.auth.models import User

# from datetime import datetime
# from django.utils import timezone
from datetime import datetime, timedelta


# from django.contrib.auth.mixins import LoginRequiredMixin

# @allowed_users(allowed_roles=['admin'])
@login_required(login_url='/user/login/')
# @admin_only
def dashboard(request):
	# customer = Customer.objects.get(pk=cid)
	customers = Customer.objects.all()
	total_customers = customers.count()
	orders = Order.objects.all()

	total_orders = orders.count()
	products = Product.objects.all()
	total_products = products.count()
	# filter la choose(search)  garxa and all pending lai count garxa
	pending = orders.filter(status='Pending').count()
	delivered = orders.filter(status="Delivered").count()

	myFilter = CustomerFilter(request.GET, queryset=customers)
	customers = myFilter.qs  # in jinja this customers goes

	# today_date = datetime.today()#filter every day order product for daily expenses

	# today_customers = customers.filter(date_created__year = today_date.year,date_created__month = today_date.month,
	#                                 date_created__day = today_date.day).count()

	# details of last 24 hours#b4 i also get same output using above line but now not so use this concept
	today_customers = customers.filter(
		date_created__gte=datetime.now() - timedelta(days=1)).count()
	# today_order = orders.filter(created_at__year = today_date.year,created_at__month = today_date.month,created_at__day = today_date.day)
	# A timedelta object represents a duration, the difference between two dates or times.
	today_order = orders.filter(
		created_at__gte=datetime.now() - timedelta(days=1))

	order_total_price = 0.00

	for order in today_order:
		per_total_price = float(order.product.price) * order.quantity
		order_total_price += per_total_price

	print(order_total_price)

	# customer = Customer.objects.get(pk=cid) #but i need pk = cid(update)
	# particular_customer_price=0.00
	# for order in customer.order_set.all():
	# 	per_total_price = float(order.product.price) * order.quantity
	# 	particular_customer_price += per_total_price
	context = {
		'customers': customers, 'orders_total_price': order_total_price, 'total_orders': total_orders,
		'myFilter': myFilter, 'today_customers': today_customers, 'current_data': datetime.now(),
		'orders_pending': pending, 'orders_delivered': delivered, 'total_products': total_products, 'total_customers': total_customers
	}

	return render(request, 'registers/index.html', context)


# Create your views here.
def first_page(request):
	current_date = datetime.now()

	return render(request, 'registers/firstpage.html', {'current_date': current_date})


@unauthenticated_user
def loginPage(request):
    
	if request.user.is_authenticated:
		return redirect('/')

	if request.method == 'POST':

		email = request.POST.get('email')  # grabing email from field
		password = request.POST.get('password')

		# Little Hack to work around re-building the usermodel
		try:
			user = User.objects.get(email=email)
			user = authenticate(
				request, username=user.username, password=password)
		except:
			messages.error(request, 'User with this email does not exists')
			return redirect('register_app:login')

		if user is not None:
			login(request, user)
			return redirect('home')
		else:
			messages.error(request, 'Email OR password is incorrect')

	context = {}
	return render(request, 'registers/login.html', context)


@unauthenticated_user
def SignupView(request):

	form = SignupForm()

	if request.method == 'POST':

		form = SignupForm(request.POST)

		if form.is_valid():
			user = form.save(commit=False)
			user.save()
			
			# group = Group.objects.get(name='Employee)
			# any time a user signup it is associated with employee group directly
			role = form.cleaned_data.get('role')
			group = Group.objects.get(name=role)
			user.groups.add(group)
			messages.success(request, 'Account successfuly created!')

			user = authenticate(
				   request, username=user.username, password=request.POST['password1'])

			next_url = request.GET.get('next')

			if next_url == '' or next_url == None:
				next_url = 'register_app:login'

			return redirect(next_url)

		else:
			messages.error(request, 'An error has occured with registration')

	context = {'form': form}
	return render(request, 'registers/register.html', context)




def logoutUser(request):
	logout(request)
	return redirect('register_app:login')


# @admin_only
# def adminProfile(request):
#     return render(request,'registers/admin_view.html')

# below package is for changing password form


def UserProfile(request):

	defaultForm = UpdateDefaultProfile(instance=request.user)
	customForm = UpdateCustomProfile(instance=request.user.profile)
	PassForm = PasswordChangeForm(request.user)

	if request.method == 'POST' and 'profile_edit' in request.POST:  # name = profile_edit in submit button
		defaultForm = UpdateDefaultProfile(request.POST, instance=request.user)
		customForm = UpdateCustomProfile(
			request.POST, request.FILES, instance=request.user.profile)

		if defaultForm.is_valid() and customForm.is_valid():
			defaultForm.save()
			customForm.save()

			messages.success(request, "Your record is successfully updated")
			return redirect('register_app:user_view')

	if request.method == 'POST' and 'change_pass_button' in request.POST:

		# i dnot see instance when changing password
		PassForm = PasswordChangeForm(user=request.user, data=request.POST)

		if PassForm.is_valid():
			PassForm.save()
			update_session_auth_hash(request, PassForm.user)  # Important!
			messages.success(request, "Your password is successfully updated")
			return redirect('register_app:user_view')

	return render(request, 'registers/edit_user.html', {'defaultForm': defaultForm, 'customForm': customForm, 'PassForm': PassForm})
