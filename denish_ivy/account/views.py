from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .froms import OrderForm, CreateUserForm
from .filters import OrderFilter

def registerPage(request):
	# if request.user.is_authenticated:
	# 	return redirect('home')
	# else:
	# 	form = CreateUserForm()
	# 	if request.method == 'POST':
	# 		form = CreateUserForm(request.POST)
	# 		if form.is_valid():
	# 			form.save()
	# 			user = form.cleaned_data.get('username')
	# 			messages.success(request, 'Account was created for ' + user)

	# 			return redirect('login')
			

		context = {'form':form}
		return render(request, 'account/register.html', context)

def loginPage(request):
    

		context = {}
		return render(request, 'account/login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')


# Create your views here.
def home(request):
    order = Order.objects.all()
    customer = Customer.objects.all()

    total_customer = customer.count()
    total_deliverd = order.filter(status = 'Deliverd').count()
    total_orders = order.count()
    Pending = order.filter(status = 'Pending').count()

    content = {'order': order, 'customer': customer, 'total_deliverd' : total_deliverd, 'Pending' : Pending, 'total_orders': total_orders}

    return render(request, 'account/dashboard.html', content)

def product(request):
    product = Product.objects.all()
    return render(request, 'account/product.html', {'product':product})


def customer(request, pk):

    customer=Customer.objects.get(id=pk)
    
    orders = customer.order_set.all()
    order_count = orders.count()

    context = {'customer': customer, 'orders': orders, 'order_count': order_count}
    return render(request, 'account/customer.html', context)


def createOrder(request):  
    form = OrderForm(initial={'form': customer})
    if request.method == 'POST':
         form=OrderForm(request.POST)
         if form.is_valid():
             form.save() 
             return redirect('/')

    context={'form':form}
    return render(request, 'account/order_form.html', context)


def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
         form=OrderForm(request.POST, instance=order)
         if form.is_valid():
             form.save() 
             return redirect('/')
    context={'form':form}
    return render(request, 'account/order_form.html', context)


def deletOrder(request, pk):   
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')

    context={'item':order}
    return render(request, 'account/delet.html', context)

#def customerMain(request):
 #   customer = Customer.objects.all()
  #  return render(request, 'account/customer.html', {'customer':customer})

