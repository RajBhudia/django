from django.shortcuts import render

# Create your views here.
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'account/dashboard.html')

def product(request):
    return render(request, 'account/product.html')


def customer(request):
    return render(request, 'account/customer.html')
