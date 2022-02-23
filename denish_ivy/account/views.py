from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.views import View
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required



from django.views.generic.list import ListView

from django.views.generic.base import TemplateView

from account.models import Customer, Product

from django.shortcuts import get_object_or_404
from django.views.generic.base import RedirectView

# Create your views here.
from .models import *
from .forms import OrderForm, CreateUserForm
from .filters import OrderFilter

def registerPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form = CreateUserForm()
		if request.method == 'POST':
			form = CreateUserForm(request.POST)
			if form.is_valid():
				form.save()
				user = form.cleaned_data.get('username')
				messages.success(request, 'Account was created for ' + user)

				return redirect('login')
			

		context = {'form':form}
		return render(request, 'account/register.html', context)

def loginPage(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'account/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')


@login_required(login_url='login')
def home(request):
	orders = Order.objects.all()
	customers = Customer.objects.all()

	total_customers = customers.count()

	total_orders = orders.count()
	delivered = orders.filter(status='Delivered').count()
	pending = orders.filter(status='Pending').count()

	context = {'orders':orders, 'customers':customers,
	'total_orders':total_orders,'delivered':delivered,
	'pending':pending }

	return render(request, 'account/dashboard.html', context)

@login_required(login_url='login')
def products(request):
	products = Product.objects.all()

	return render(request, 'account/products.html', {'products':products})

@login_required(login_url='login')
def customer(request, pk_test):
	customer = Customer.objects.get(id=pk_test)

	orders = customer.order_set.all()
	order_count = orders.count()

	myFilter = OrderFilter(request.GET, queryset=orders)
	orders = myFilter.qs 

	context = {'customer':customer, 'orders':orders, 'order_count':order_count,
	'myFilter':myFilter}
	return render(request, 'account/customer.html',context)

@login_required(login_url='login')
def createOrder(request, pk):
	OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=2 )
	customer = Customer.objects.get(id=pk)
	formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
	#form = OrderForm(initial={'customer':customer})
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = OrderForm(request.POST)
		formset = OrderFormSet(request.POST, instance=customer)
		if formset.is_valid():
			formset.save()
			return redirect('/')

	context = {'form':formset}
	return render(request, 'account/order_form.html', context)

@login_required(login_url='login')
def updateOrder(request, pk):

	order = Order.objects.get(id=pk)
	form = OrderForm(instance=order)

	if request.method == 'POST':
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request, 'account/order_form.html', context)

@login_required(login_url='login')
def deleteOrder(request, pk):
	order = Order.objects.get(id=pk)
	if request.method == "POST":
		order.delete()
		return redirect('/')

	context = {'item':order}
	return render(request, 'account/delet.html', context)

##########################################################################################################
"""view base class base view"""

class MyView(View):

		"""This is master class base view. all othwer class base inherit from it.

		some of the HTTP method view can accept are ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']"""

		def get(self, request, *args, **kwargs):
			return HttpResponse('Hello, World!')



class HomePageView(ListView):

	model = Product
	def get(self, request):
		return (self, 'products.html')



class Customer1View(View):

	"""have to research on it exact use of it, pending"""

	"""It helps us to render templates context with given URL"""
	template_name = ''

	def get_context_data(self, request, pk_test):
		customer = Customer.objects.all(id=pk_test) 
		return render(request, self.template_name, {'customer':customer})
		

class ProductView(View):
	def get(self, request):
		products = Product.objects.all()
		return render(request, 'account/products.html', {'products':products})
       
       

class DashboardView(View):
	def get(self, request):
		return render(request, 'account/dashboard.html')

class CustomerView(View):
	def get(self, request, pk_test):

		customer = Customer.objects.get(id=pk_test)

		orders = customer.order_set.all()
		order_count = orders.count()

		myFilter = OrderFilter(request.GET, queryset=orders)
		orders = myFilter.qs 

		context = {'customer':customer, 'orders':orders, 'order_count':order_count,
		'myFilter':myFilter}
		return render(request, 'account/customer.html',context)


class CreateOrderView(View):
	def get(self, request, pk):
		OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=2 )
		customer = Customer.objects.get(id=pk)
		formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
		#form = OrderForm(initial={'customer':customer})
		if request.method == 'POST':
			#print('Printing POST:', request.POST)
			form = OrderForm(request.POST)
			formset = OrderFormSet(request.POST, instance=customer)
			if formset.is_valid():
				formset.save()
				return redirect('/')

		context = {'form':formset}
		return render(request, 'account/order_form.html', context)


class RegisterView(View):
	# def get(self, request):
	# 	if request.user.is_authenticated:
	# 		return redirect('home')		
	def post(self, request):
		form = CreateUserForm()
		form = CreateUserForm(request.POST)
		if form.is_valid():
			form.save()
			user = form.cleaned_data.get('username')
			messages.success(request, 'Account was created for ' + user)
			return redirect('login')
						

		context = {'form':form}
		return render(request, 'account/register.html', context)

class UpdateOrderView(View):
	# def get(self, request, pk):
	# 	order = Order.objects.get(id=pk)
	# 	forms = OrderForm(instance=order)
	# 	# return render(request, 'account/order_form.html')
	def post(self, request, pk):
		order = Order.objects.get(id=pk)
		form = OrderForm(request.POST, instance=order)
		if form.is_valid():
			form.save()
			return redirect('/')

		context = {'form':form}
		return render(request, 'account/order_form.html', context)

class DeletOrderView(View):
	def get(self, request, pk):
		order = Order.objects.get(id=pk)
		if request.method == "POST":
			order.delete()
			return redirect('/')

		context = {'item':order}
		return render(request, 'account/delet.html', context)



###################################################
"""Templates views"""

# #class TemplateView(TemplatesResponseMixin, ContentMixin, view)
# it will use all 3 names given in brackets and in hertit them 

"""with th help of template view we can redirect URl"""

# class HomeTemplateView(TemplateView):
#  template_name = 'account/customer.html'

class HomeTemplateView(TemplateView):
 template_name = 'account/dashboard.html'

 def get_context_data(self, **kwargs):
	 
		orders = Order.objects.all()
		customers = Customer.objects.all()

		total_customers = customers.count()

		total_orders = orders.count()
		delivered = orders.filter(status='Delivered').count()
		pending = orders.filter(status='Pending').count()

		context = {'orders':orders, 'customers':customers,
		'total_orders':total_orders,'delivered':delivered,
		'pending':pending }
		return context

"""context = super().get_context data(**kwargs) with the help of this we can add data in html page
	ex:- context['demo'] = trail,  just add demo in html form tag it will show trail in output"""


#########################################################################
"""RedirectView"""
"""It is use to redirect to given or predefine example
	if http://127.0.0.1:8000/ is home url  
	and if we hit  url like this http://127.0.0.1:8000/index or home it will redirect to http://127.0.0.1:8000/ instead of showing index or home"""
""" Common use is to hit """

class GeetRedirectView(RedirectView):
 pattern_name = 'mindex'
 permanent = True
 query_string = True

 def get_redirect_url(self, *args, **kwargs):
  print(kwargs)
  kwargs['pk'] = 16
  return super().get_redirect_url(*args, **kwargs)

