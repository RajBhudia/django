from django.shortcuts import render
from .models import *

custom = Customer.objects.all()
print('1.every person', custom)
print('2.first person', custom.first())

custom1 = Customer.objects.get(name='Raj')
print('3 single', custom1)
print('4.email', custom1.email)
print('5 id', custom1.id)


custom3 = Customer.objects.get(id=1)
custom4 = custom3.order_set.all()
print('oder of id1=', custom4)
print('3rd id name=', custom3)


custom5 = Order.objects.first()
print('first to oder=',custom5)
print('mobile no = ', custom5.customer.phone)


custom6 = Product.objects.filter(category = 'Outdor')
print('item name = ', custom6)

custom7 = Product.objects.filter(category = 'Outdor').order_by('-id')
print('out will be in last to first form = ', custom7)


custom8 = Product.objects.filter(tag__name = 'KITCHEN')
print('retriving data from many2many=', custom8)



